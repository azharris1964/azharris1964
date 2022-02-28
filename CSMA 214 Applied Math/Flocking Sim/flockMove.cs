using System.Collections;
using System.Collections.Generic;
using UnityEngine;


// Armontae Harris  Flocking Project


// included the comments for the different actions (Pseudocode)
// added new interactive variable (goal position)
// added bounding box 

public class flockMove : MonoBehaviour
{
    //creates speed variable
    public float speed;

    public FlockManager myManager;

    bool turn = false;

    // Start is called before the first frame update
    void Start()
    {
        speed = Random.Range(myManager.minSpeed, myManager.maxSpeed);
    }

    // Update is called once per frame
    void Update()
    {
        //bounding box for manager
        Bounds b = new Bounds(myManager.transform.position, myManager.limit*2);

        // decides to turn or not
        if(!b.Contains(transform.position))
        {
            turn = true;
        }
        else
            turn = false; 

        // changes direction if turn is on
        if(turn)
        {
            // creates new direction back to center
            Vector3 direction = myManager.transform.position - transform.position;
            transform.rotation = Quaternion.Slerp(transform.rotation, 
                                                    Quaternion.LookRotation(direction), 
                                                    myManager.comfortDistance * Time.deltaTime);
        }
        else
        {
            // resets the speed randmonly
            if(Random.Range(0, 100) < 10)
                speed = Random.Range(myManager.minSpeed,
                                     myManager.maxSpeed);

            // stops the rules from happening every frame (20% of time)
            if(Random.Range(10, 100) < 20)
                flockRules();

            
        }

        transform.Translate(0, 0, Time.deltaTime * speed);
    }

    void flockRules()
    {
        GameObject[] gos;
        gos = myManager.allFlockObj;

        // center of group      : Vector3
        Vector3 vCenter = Vector3.zero;

        // avoid direction      : Vector3
        Vector3 vAvoid = Vector3.zero;

        // group speed          : Float
        float groupSpeed = 0.01f;

        // neighbor distance    : Float
        float neighborDistance;

        // group size           : Int
        int groupSize = 0;

        // runs for every objects
        foreach (GameObject go in gos) 
        {
            // determines how to move with group
            if (go != this.gameObject)
            {
                // distance between this object and gO 
                neighborDistance = Vector3.Distance(go.transform.position, this.transform.position);

                // if object is within neighbor distance
                if (neighborDistance <= myManager.neighborDistance)
                {
                    // creates new center
                    vCenter += go.transform.position;

                    groupSize++;
                 
                    // if within neighbor distance
                    if (neighborDistance < 1.0f)
                    {
                    // avoid if too close
                        vAvoid = vAvoid + (this.transform.position - go.transform.position);
                    }
                    // define flock speed
                    flockMove anotherFlock = go.GetComponent<flockMove>();

                    // define group speed
                    groupSpeed = groupSpeed + anotherFlock.speed;

                }
            }
        }

        // if group bigger than 0
        if (groupSize > 0)
        {
            // define object group center
            vCenter = vCenter / groupSize + (myManager.goalPos - this.transform.position);

            //  define speed of group as average of other members
            speed = groupSpeed / groupSize;

            // define  travel direction
            Vector3 direction = (vCenter + vAvoid) - transform.position;

            if (direction != Vector3.zero)
            
                transform.rotation = Quaternion.Slerp(transform.rotation,
                                                        Quaternion.LookRotation(direction),
                                                        myManager.comfortDistance * Time.deltaTime);
            


        }


    }
}
