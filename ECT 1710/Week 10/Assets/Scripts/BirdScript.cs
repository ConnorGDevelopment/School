using UnityEngine;

public class BirdScript : MonoBehaviour
{
    public Rigidbody2D RigidBody;
    public float FlapStrength;
    public LogicScript Logic;
    public bool IsBirdAlive = true;

    // Start is called before the first frame update
    void Start()
    {
        if (gameObject.TryGetComponent(out Rigidbody2D rigidbody))
        {
            RigidBody = rigidbody;
        }
        else
        {
            Debug.Log("No Rigidbody", gameObject);
        }
        Logic = GameObject.FindGameObjectWithTag("Logic").GetComponent<LogicScript>();
    }

    public void Flap()
    {
        RigidBody.velocity = Vector2.up * FlapStrength;
    }
    private void OnCollisionEnter2D(Collision2D collision)
    {
        Logic.gameOver();
        IsBirdAlive = false;
    }
}
