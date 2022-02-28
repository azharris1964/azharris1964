using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class FlockManager : MonoBehaviour 
{
    // boid game object
    public GameObject flockObj;

    // holds flock objects
    public GameObject flockContainer;

    // array of game objects that hold boids
    public int numObj = 20;

    // an int to define how many onjects are in the array of game objects
    public GameObject[] allFlockObj;

    // instantiation boundary
    public Vector3 limit = new Vector3(5, 5, 5);

    //creates gaol variable
    public Vector3 goalPos;

    // global variables
    [Header ("Flock Attributes")]

    [Range(0.0f, 5.0f)]
    public float minSpeed;      // minspeed of flocking object

    [Range(0.0f, 5.0f)]
    public float maxSpeed;         // maxspeed of flocking object

    [Range(1.0f, 10.0f)]           
    public float neighborDistance;   // distance radius

    [Range(1.0f, 5.0f)]             
    public float comfortDistance;   // comfort distance



    // Start is called before the first frame update
    void Start()
    {
        // use numObj to create allFlockObj array
        allFlockObj = new GameObject[numObj];
        // for loop
        for (int i = 0; i < numObj; i++)
        {
            // generate a random object
            Vector3 pos = this.transform.position + new Vector3(Random.Range(-limit.x, limit.x),
                                                                Random.Range(-limit.y, limit.y),
                                                                Random.Range(-limit.z, limit.z));

            //Vector3 scale = new Vector3(Random.Range(0.1f, 1), Random.Range(0.1f, 1), Random.Range(0.1f, 1));
            // place our GameObject as the generate point
            allFlockObj[i] = (GameObject) Instantiate(flockObj, pos, Quaternion.identity);

            // place instantiated object as a child of an empty GameObject
            allFlockObj[i].transform.parent = flockContainer.transform;

            // add the flock manager to objects being instantiated
            allFlockObj[i].GetComponent<flockMove>().myManager = this;

            // how can we instantiate at different sizes
            //allFlockObj[i].transform.localScale;

        }

        // defines goal position
        goalPos = this.transform.position;


    }

    // Update is called once per frame
    void Update()
    {
        // updates goal position within boundary
        if (Random.Range(0, 100) < 10)
            goalPos = this.transform.position + new Vector3(Random.Range(-limit.x, limit.x),
                                                            Random.Range(-limit.y, limit.y),
                                                            Random.Range(-limit.z, limit.z));
    }
}
