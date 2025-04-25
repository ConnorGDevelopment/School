// I worked with something like this in Unity, didn't realize it was a base thing

using System.Numerics;

public class Vector2Int
{
    public int X = 0;
    public int Y = 0;

    // Filling in Vector properties so later code is cleaner
    public Vector2Int Right
    {
        get { return new(X + 1, Y); }
    }

    public Vector2Int Left
    {
        get { return new(X - 1, Y); }
    }

    public Vector2Int Up
    {
        get { return new(X, Y + 1); }
    }

    public Vector2Int Down
    {
        get { return new(X, Y - 1); }
    }

    public List<Vector2Int> Adjacent
    {
        get { return [Right, Left, Up, Down]; }
    }

    public Vector2Int(int x, int y)
    {
        X = x;
        Y = y;
    }
}

public class GameObject
{
    public Vector2Int Position;

    // This is so LocalMap can manipulate the object even when it is passed as a reference

    // This is so EnemyShip can override for cloaking
    protected char _mapSymbol;
    public virtual char MapSymbol
    {
        get { return _mapSymbol; }
    }

    public GameObject(char mapSymbol, Vector2Int position)
    {
        _mapSymbol = mapSymbol;
        Position = position;
    }
}

public class Ship : GameObject
{
    public string Name;
    public int Energy;
    public readonly int MaximumEnergy = 1000;

    public int Torpedoes;

    public Ship(
        string name,
        char mapSymbol,
        Vector2Int position,
        int energy = 1000,
        int torpedoes = 10
    )
        : base(mapSymbol, position)
    {
        Name = name;
        Energy = energy;
        Torpedoes = torpedoes;
    }
}

public class EnemyShip : Ship
{
    public bool Cloak;

    public override char MapSymbol
    {
        get { return Cloak ? '?' : _mapSymbol; }
    }

    public EnemyShip(
        string name,
        char mapSymbol,
        Vector2Int position,
        int energy = 1000,
        int torpedoes = 10
    )
        : base(name, mapSymbol, position, energy, torpedoes)
    {
        Cloak = RandHelper.FiftyFifty();
    }
}

public class FederationShip : Ship
{
    public FederationShip(
        string name,
        char mapSymbol,
        Vector2Int position,
        int energy = 1000,
        int torpedoes = 10
    )
        : base(name, mapSymbol, position, energy, torpedoes) { }
}

public class Starbase : GameObject
{
    public string Name;

    public Starbase(string name, Vector2Int position)
        : base('#', position)
    {
        Name = name;
    }
}

public class Star : GameObject
{
    public Star(Vector2Int position)
        : base('*', position) { }
}

public class LocalMap
{
    private List<GameObject> GameObjects = [];

    private readonly int RowLength;
    private readonly int ColumnLength;

    public LocalMap(int rowLength, int columnLength)
    {
        RowLength = rowLength;
        ColumnLength = columnLength;
    }

    // Constructing the Map

    // Making the header
    private string MapHeader
    {
        get
        {
            string header = " ";
            for (int row = 0; row < RowLength; row++)
            {
                header += $" {row}";
            }
            return header;
        }
    }

    // Makes a blank map then fills in markers
    private char[,] RawMapBody
    {
        get
        {
            char[,] rawMap = new char[RowLength, ColumnLength];

            // Fill with '.'
            for (int row = 0; row < RowLength; row++)
            {
                for (int col = 0; col < ColumnLength; col++)
                {
                    rawMap[row, col] = '.';
                }
            }

            // Mark where gameObjects are using their coordinates
            foreach (var gameObject in GameObjects)
            {
                rawMap[gameObject.Position.X, gameObject.Position.Y] = gameObject.MapSymbol;
            }

            return rawMap;
        }
    }

    // Formats RawMapBody with the columns on the sides and spacing between points
    private string[] MapBody
    {
        get
        {
            // Make a string array to simplify reading off the lines
            string[] mapBody = new string[RowLength];

            for (int row = 0; row < RowLength; row++)
            {
                char[] rawLine = new char[RowLength];

                // Because you can't just grab a row of a 2D array
                for (int col = 0; col < ColumnLength; col++)
                {
                    rawLine[col] = RawMapBody[row, col];
                }

                // Add in row markers
                string line = $"{row} {string.Join(" ", rawLine)} {row}";

                mapBody[row] = line;
            }

            return mapBody;
        }
    }

    // Draws all of the pieces together
    public void Display()
    {
        Console.WriteLine(MapHeader);
        foreach (var line in MapBody)
        {
            Console.WriteLine(line);
        }
        Console.WriteLine(MapHeader);
    }

    // Coordinate Manipulations
    // Get all possible coordinates (Set A)
    private List<Vector2Int> AllCords
    {
        get
        {
            List<Vector2Int> allCords = [];

            for (int row = 0; row < RowLength; row++)
            {
                for (int col = 0; col < ColumnLength; col++)
                {
                    allCords.Add(new(row, col));
                }
                ;
            }

            return allCords;
        }
    }

    // Get all coordinates with an object in them (Set A - Set B)
    private List<Vector2Int> OccupiedCords
    {
        get
        {
            List<Vector2Int> occupiedCords = [];

            foreach (var gameObject in GameObjects)
            {
                occupiedCords.Add(gameObject.Position);
            }

            return occupiedCords;
        }
    }

    // Get all coordinates without an object in them (Set A - (Set A - Set B))
    private List<Vector2Int> EmptyCords
    {
        get
        {
            List<Vector2Int> emptyCords = [];

            foreach (var coordinate in AllCords)
            {
                var match = OccupiedCords.Find(
                    (occupiedCoordinate) =>
                        (occupiedCoordinate.X == coordinate.X)
                        && (occupiedCoordinate.Y == coordinate.Y)
                );

                if (match == null)
                {
                    emptyCords.Add(coordinate);
                }
            }

            return emptyCords;
        }
    }

    // Ships can spawn at any unoccupied point that is not adjacent to a Starbase
    private List<Vector2Int> ValidShipSpawnCords
    {
        get
        {
            List<Vector2Int> validShipSpawnCords = EmptyCords;

            foreach (var gameObject in GameObjects)
            {
                if (gameObject is Starbase)
                {
                    var starbase = (Starbase)gameObject;

                    foreach (var delta in starbase.Position.Adjacent)
                    {
                        var match = validShipSpawnCords.Find((cord) => cord == delta);

                        if (match != null)
                        {
                            validShipSpawnCords.Remove(match);
                        }
                    }
                }
            }

            return validShipSpawnCords;
        }
    }

    // Starbases can spawn at any unoccupied point
    private List<Vector2Int> ValidStarbaseSpawnCords
    {
        get { return EmptyCords; }
    }

    private List<Vector2Int> ValidStarSpawnCords
    {
        get { return EmptyCords; }
    }

    // Pulls one random point from all valid Ship spawn cords
    private Vector2Int RandValidShipSpawnCord()
    {
        return RandHelper.FromSet(ValidShipSpawnCords);
    }

    // Pulls one random point from all valid Starbase spawn cords
    private Vector2Int RandValidStarbaseSpawnCord()
    {
        return RandHelper.FromSet(ValidStarbaseSpawnCords);
    }

    // Same as Starbase, renaming for code clarity
    private Vector2Int RandValidStarSpawnCord()
    {
        return RandHelper.FromSet(ValidStarSpawnCords);
    }

    // Spawning Units
    // Naming these methods after the List methods
    // I've seen in the Microsoft C# docs examples where they define a custom Equals() method
    // In Javascript I've had to do that for the toJSON() method for classes, because the Vuex store system had issues holding non-POJOs (Plain Old Java Object)
    // I never really understood why you would do it for an Equals() method until now
    // It lets you make shortcuts to inner props and stuff and interact with the class like it were a core type
    private void Append(GameObject gameObject)
    {
        GameObjects.Add(gameObject);
    }

    // private void Remove(GameObject gameObject)
    // {
    //     GameObjects.Remove(gameObject);
    // }

    // Semi-irrelevant, makes sure two ships don't have the same name
    private List<string> UsedNames
    {
        get
        {
            List<string> usedNames = [];

            foreach (GameObject gameObject in GameObjects)
            {
                if (gameObject is Ship)
                {
                    // My linter suggested I do this instead of "as Ship"
                    // In Typescript "as" usually just casts it to that type, I don't fully understand what the difference is in C#
                    // This is definitely outside of class + my experience, but its for a fun name generator so shouldn't be an issue
                    Ship _gameObject = (Ship)gameObject;
                    usedNames.Add(_gameObject.Name);
                }
                else if (gameObject is Starbase)
                {
                    Starbase _gameObject = (Starbase)gameObject;
                    usedNames.Add(_gameObject.Name);
                }
            }

            return usedNames;
        }
    }

    public void DeepScan()
    {
        foreach (var name in UsedNames)
        {
            Console.WriteLine(name);
        }
    }

    public void SpawnKlingon()
    {
        Append(new EnemyShip(RandHelper.RandKlingon(UsedNames), 'K', RandValidShipSpawnCord()));
    }

    public void SpawnRomulan()
    {
        Append(new EnemyShip(RandHelper.RandRomulan(UsedNames), 'R', RandValidShipSpawnCord()));
    }

    public void SpawnEnterprise()
    {
        Append(new FederationShip("Enterprise", 'E', RandValidShipSpawnCord()));
    }

    public void SpawnStarbase()
    {
        Append(new Starbase(RandHelper.RandStarbase(UsedNames), RandValidStarbaseSpawnCord()));
    }

    public void SpawnStar()
    {
        Append(new Star(RandValidStarSpawnCord()));
    }

    // Spawn Order
    // 1. Stars
    // 2. Starbases
    // 3. Enterprise
    // 3. Klingons and Romulans
    public void Spawn(
        int klingonCount,
        int romulanCount,
        int starbaseCount,
        (int, int) starCountRangeBounds
    )
    {
        // Apparently you can't iterate over ranges by default, so have to fill a list with the values
        List<int> starCountRange = [];

        for (int sr = starCountRangeBounds.Item1; sr < starCountRangeBounds.Item2; sr++)
        {
            starCountRange.Add(sr);
        }

        // Take the array of potential values and pick one
        var starCount = RandHelper.FromSet(starCountRange);

        for (int s = 0; s < starCount; s++)
        {
            SpawnStar();
        }

        for (int sb = 0; sb < starbaseCount; sb++)
        {
            SpawnStarbase();
        }

        for (int k = 0; k < klingonCount; k++)
        {
            SpawnKlingon();
        }

        for (int r = 0; r < romulanCount; r++)
        {
            SpawnRomulan();
        }

        SpawnEnterprise();
    }

    // User Commands
    public void Srs()
    {
        Display();
    }

    // It took me so long to remember the modulo function, I did this with absolute values at first
    Vector2Int DegToVec(float degrees)
    {
        var correctedDegrees = (int)Math.Round(degrees % 360 / 90);

        if (correctedDegrees == 0 || correctedDegrees == 4)
        {
            Console.WriteLine("Left");
            return new(0, -1);
        }
        else if (correctedDegrees == 1)
        {
            Console.WriteLine("Up");
            return new(-1, 0);
        }
        else if (correctedDegrees == 2)
        {
            Console.WriteLine("Right");
            return new(0, 1);
        }
        else if (correctedDegrees == 3)
        {
            Console.WriteLine("Down");
            return new(1, 0);
        }
        else
        {
            // Failsafe, doesn't move
            return new(0, 0);
        }
    }

    private List<Vector2Int> AllStarbaseCords
    {
        get
        {
            List<Vector2Int> allStarbaseCords = [];

            foreach (var gameObject in GameObjects)
            {
                if (gameObject is Starbase)
                {
                    allStarbaseCords.Add(gameObject.Position);
                }
            }
            ;

            return allStarbaseCords;
        }
    }

    private void MoveShip(FederationShip enterprise, Vector2Int destination)
    {
        enterprise.Position = destination;

        foreach (var starbaseCords in AllStarbaseCords)
        {
            var match = enterprise.Position.Adjacent.Find(
                (adjPos) => adjPos.X == starbaseCords.X && adjPos.Y == starbaseCords.Y
            );
            if (match != null)
            {
                Console.WriteLine("Docked at Starbase");
                enterprise.Energy = enterprise.MaximumEnergy;
            }
        }
    }

    private void MoveError(Vector2Int destination)
    {
        var matchOther = GameObjects.Find(
            (other) => other.Position.X == destination.X && other.Position.Y == destination.Y
        );
        if (matchOther != null)
        {
            Console.WriteLine(matchOther.MapSymbol);
            if (matchOther.MapSymbol == 'K')
            {
                Console.WriteLine(
                    "Captain, that course would ram us straight into that ship! That Klingon ship!"
                );
            }
            else if (matchOther.MapSymbol == 'R')
            {
                Console.WriteLine(
                    "Captain, I don't think our insurance covers intentionally ramming a Romulan ship."
                );
            }
            else if (matchOther.MapSymbol == '?')
            {
                Console.WriteLine(
                    "Captain, the scanners say that space is not so empty. I suggest another course."
                );
            }
            else if (matchOther.MapSymbol == '#')
            {
                Console.WriteLine(
                    "Captain, I recommend going around to park instead of through. And by recommend, I mean insist."
                );
            }
            else if (matchOther.MapSymbol == '*')
            {
                Console.WriteLine(
                    "Captain, we can't take that course. I forgot my star-proof anatomy at home."
                );
            }
            else
            {
                Console.WriteLine(
                    "To boldly go where no man has gone before! (We can't move in that direction)"
                );
            }
        }
        else
        {
            Console.WriteLine(
                "To boldly go where no man has gone before! (We can't move in that direction)"
            );
        }
    }

    public void Move(float degrees)
    {
        GameObject? _enterprise = GameObjects.Find(
            (gameObject) => gameObject.MapSymbol == 'E' && gameObject is FederationShip
        );

        if (_enterprise != null)
        {
            FederationShip enterprise = (FederationShip)_enterprise;
            Console.WriteLine($"{enterprise.Position.X},{enterprise.Position.Y}");

            Vector2Int destination =
                new(
                    enterprise.Position.X + DegToVec(degrees).X,
                    enterprise.Position.Y + DegToVec(degrees).Y
                );

            Console.WriteLine($"{destination.X},{destination.Y}");
            // Console.WriteLine($"{EmptyCords.Count}");

            var match = EmptyCords.Find(
                (cords) => cords.X == destination.X && cords.Y == destination.Y
            );

            if (match != null)
            {
                MoveShip(enterprise, destination);
            }
            else
            {
                MoveError(destination);
            }

            Display();
        }
    }
}
