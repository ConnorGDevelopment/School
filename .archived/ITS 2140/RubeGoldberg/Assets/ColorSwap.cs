using UnityEngine;
public enum ColorKeys {
    zero,
    one,
    two,
    three,
}

public class ColorSwap : MonoBehaviour {


    public ColorKeys Name;
    public string Color;

    public void ChangeColor(string hexColor) {
        ColorUtility.TryParseHtmlString(hexColor, out Color color);
        Color = hexColor;
        gameObject.GetComponent<MeshRenderer>().material.SetColor("_Color", color);
    }

}
