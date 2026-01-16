using UnityEngine;
using UnityEngine.AI;



public class ColorBump : MonoBehaviour {
    [System.Serializable]
    public class LegoColors {
        public string zero;
        public string one;
        public string two;
        public string three;

        public static LegoColors CreateFromJson(string jsonString) {
            return JsonUtility.FromJson<LegoColors>(jsonString);
        }
    }

    public LegoColors legoColors;

    public class Destinations {
        public bool zero = false;
        public bool one = false;
        public bool two = false;
        public bool three = false;
    }

    public Destinations Targets = new();

    public void SetDestination() {
        if (!Targets.zero) {
            gameObject.GetComponent<NavMeshAgent>().destination = GameObject.Find("Zero").transform.position;
        } else if (!Targets.one) {
            gameObject.GetComponent<NavMeshAgent>().destination = GameObject.Find("One").transform.position;
        } else if (!Targets.two) {
            gameObject.GetComponent<NavMeshAgent>().destination = GameObject.Find("Two").transform.position;
        } else if (!Targets.three) {
            gameObject.GetComponent<NavMeshAgent>().destination = GameObject.Find("Three").transform.position;
        } else {
            gameObject.GetComponent<NavMeshAgent>().destination = Home;
        }
    }

    public void OnCollisionEnter(Collision collision) {
        if (collision.gameObject.TryGetComponent(out ColorSwap colorSwap)) {
            var color = "";
            if (collision.gameObject.name == "Zero") {
                color = legoColors.zero;
                Targets.zero = true;
            } else if (collision.gameObject.name == "One") {
                color = legoColors.one;
                Targets.one = true;
            } else if (collision.gameObject.name == "Two") {
                color = legoColors.two;
                Targets.two = true;
            } else if (collision.gameObject.name == "Three") {
                color = legoColors.three;
                Targets.three = true;
            }
            colorSwap.ChangeColor(color);
            SetDestination();
        }
    }

    public Vector3 Home;

    public void Start() {
        Home = gameObject.transform.position;
        var json = Resources.Load<TextAsset>("lego");
        legoColors = LegoColors.CreateFromJson(json.text);
        SetDestination();
    }
}