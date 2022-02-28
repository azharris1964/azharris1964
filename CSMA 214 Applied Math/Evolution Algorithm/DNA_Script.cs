using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DNA_Script : MonoBehaviour
{
    public float r;
    public float g;
    public float b;

    public float minRot = 1f;
    public float maxRot = 20f;
    public float Rot = 200f;

    public float timeToDie = 0; // how long does it take object to die

    bool dead = false;

    // randomizes rotation
    public float RanRot;

    // obj color
    Color OBJColor;

    //renderer
    public Renderer rend;
    public Collider col;

    // Start is called before the first frame update
    void Start()
    {
        rend = GetComponent<Renderer>();
        col = GetComponent<Collider>();

        rend.material.color = new Color(r, g, b);
    }

    // Update is called once per frame
    void Update()
    {
        transform.Rotate(new Vector3(Rot, minRot * RanRot, maxRot * RanRot) * Time.deltaTime);
    }

    private void OnMouseDown()
    {
        dead = true;
        timeToDie = Population_Manager.elapsed;
        rend.enabled = false;
        col.enabled = false;
    }
}
