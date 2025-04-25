var gameMap = new LocalMap(10, 10);

gameMap.Spawn(1, 3, 1, (2, 4));

var running = true;
string? answer;

// Header Stolen from: http://www.catb.org/~esr/super-star-trek/sst-doc.html
RandHelper.StarTrekHeader();

gameMap.Display();

Console.WriteLine();

while (running)
{
    try
    {
        Console.Write("> ");
        answer = Console.ReadLine();
        if (answer == null || answer == "")
        {
            throw new ArgumentOutOfRangeException("Please type a command");
        }
        else if (answer == "q")
        {
            running = false;
        }
        else
        {
            var words = answer.Split();

            if (words[0] == "srs" || words[0] == "srscan")
            {
                gameMap.Display();
            }
            else if (words[0] == "move" || words[0] == "m")
            {
                float degrees = new();

                if (float.TryParse(words[1], out degrees))
                {
                    gameMap.Move(degrees);
                }
                else
                {
                    throw new ArgumentOutOfRangeException("Move angle invalid");
                }
            }
            else if (words[0] == "dpscan")
            {
                gameMap.DeepScan();
            }
        }
    }
    catch (Exception error)
    {
        Console.WriteLine($"Bad Input, {error.Message}");
    }
}
