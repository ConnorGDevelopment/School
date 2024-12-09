using UnityEngine;

public class PipeMoveScript : MonoBehaviour
{
    public float moveSpeed = 0.01f;
    public float deadZone = -45;

    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        transform.position = transform.position + (Vector3.left * moveSpeed);
        if (transform.position.x < deadZone)
        {
            Destroy(gameObject);
        }
    }
}
