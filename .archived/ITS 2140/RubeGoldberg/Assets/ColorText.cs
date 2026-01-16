using System.Collections.Generic;
using TMPro;
using UnityEngine;

public class ColorText : MonoBehaviour {
    public string ConvertToBinary(string colorHex) {
        if (colorHex == "#F44336") {
            return "0000";
        } else if (colorHex == "#9c27B0") {
            return "0001";
        } else if (colorHex == "#2196F3") {
            return "0010";
        } else if (colorHex == "#4CAF50") {
            return "0011";
        } else if (colorHex == "#FFEB3B") {
            return "0100";
        } else if (colorHex == "#FF9800") {
            return "0101";
        } else if (colorHex == "#795548") {
            return "0110";
        } else if (colorHex == "#212121") {
            return "1000";
        } else {
            return "";
        }
    }

    public Dictionary<ColorKeys, string> BlockColors = new();
    public TextMeshProUGUI textMesh;

    public void Start() {
        textMesh = GetComponent<TextMeshProUGUI>();
    }

    public void Update() {
        BlockColors[ColorKeys.zero] = ConvertToBinary(GameObject.Find("Zero").GetComponent<ColorSwap>().Color.ToString());
        BlockColors[ColorKeys.one] = ConvertToBinary(GameObject.Find("One").GetComponent<ColorSwap>().Color.ToString());
        BlockColors[ColorKeys.two] = ConvertToBinary(GameObject.Find("Two").GetComponent<ColorSwap>().Color.ToString());
        BlockColors[ColorKeys.three] = ConvertToBinary(GameObject.Find("Three").GetComponent<ColorSwap>().Color.ToString());

        textMesh.text = BlockColors[ColorKeys.zero] + "\n" + BlockColors[ColorKeys.one] + "\n" + BlockColors[ColorKeys.two] + "\n" + BlockColors[ColorKeys.three];
    }
}
