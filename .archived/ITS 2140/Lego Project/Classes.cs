
using System.Numerics;

public class Brick {
    public Vector3 Cords = new();
    public bool IsRotated = false;

    public enum Colors {
        Black = 0x00,
        Blue = 0x01,
        White = 0x02,
        Red = 0x03,
        Green = 0x04,
        GlossyBlack = 0x05,
        Gray = 0x06,
        Pink = 0x07,
        Yellow = 0x08,
        Orange = 0x09,
        Violet = 0x0A,
    }
    
    public readonly Colors Color;
    public Stack<Brick> Stacked = [];

    public Brick(Colors color) {
        Color = color;
    }
    public Brick(Brick brick) {
        Color = brick.Color;
        Cords = brick.Cords;
        IsRotated = brick.IsRotated;
    }

}

public class BuildPlate {
    private readonly int RowLength = 8;
    private readonly int ColumnLength = 8;
    private readonly int LayerCount = 8;

    public List<Brick> Bricks = [];
    public Brick? RegisterA = null;
    public Brick? RegisterB = null;

    public void Display() {
        for (int z = 0; z < LayerCount; z++)
        {
            Console.WriteLine("Layer: " + z);
            for(int y = 0; y < ColumnLength; y++) {
                for(int x = 0; x < RowLength; x++) {
                    Brick? brick = Bricks.Find((brick) => brick.Cords == new Vector3(x,y,z));
                    if(brick != null) {
                        Console.Write(brick.Color);
                    } else {
                        Console.Write("-");
                    }
                }
                Console.WriteLine();
            }
        }
    }

    public void Reta(Brick.Colors color) {
        RegisterA = new(color);
    }
    public void Clear() {
        RegisterA = null;
    }

    public void Swap() {
        Brick? originalRegisterA = RegisterA != null ? new(RegisterA) : null;
        Brick? originalRegisterB = RegisterB != null ? new(RegisterB) : null;

        RegisterA = originalRegisterB;
        RegisterB = originalRegisterA;
    }

    public void Rotate() {
        if(RegisterA != null) {
            RegisterA.IsRotated = !RegisterA.IsRotated;
        }
    }

    public void Add() {
        if(RegisterA != null && RegisterB != null) {
            RegisterA.Stacked.Push(new(RegisterB));
            RegisterB = null;
        }
    }

    public void Place(int x, int y, int z) {
        if(RegisterA != null) {
            RegisterA.Cords = new(x,y,z);

            foreach(var brick in RegisterA.Stacked) {
                brick.Cords = new(x,y,z + RegisterA.Stacked.Count);
                Bricks.Add(brick);
                brick.Stacked.Pop();
            }
            
            Bricks.Add(new(RegisterA));
            
            RegisterA = null;
        }
    }
}

