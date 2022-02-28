using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Linq;

public class Population_Manager : MonoBehaviour
{
    //obj to instantiate
    public GameObject ObjInstantiate;
   
    public int PopulationSize = 10;

    List<GameObject> population = new List<GameObject>();

    public int min = -5;
    public int max = 5;

    public int trialTime = 10;
    int generation = 1;
    public static float elapsed = 0;

    GUIStyle guiStyle = new GUIStyle();

    // Displays info about
    private void OnGUI()
    {
        guiStyle.fontSize = 50;
        guiStyle.normal.textColor = Color.white;
        GUI.Label(new Rect(10, 10, 100, 20), "Generation" + "");
        GUI.Label(new Rect(10, 65, 100, 20), "Trial time: " + "");
    }

    // Start is called before the first frame update
    void Start()
    {
        for (int i = 0; i < PopulationSize; i++)
        {
            // generate random position
            Vector3 pos = new Vector3(Random.Range(min, max), Random.Range(min, max), Random.Range(min, max));

            // instantiate GameObject
            GameObject gO = Instantiate(ObjInstantiate, pos, Quaternion.identity);

            gO.GetComponent<DNA_Script>().RanRot = Random.Range(10.0f, 50f);

            // define variables of GameObject
            gO.GetComponent<DNA_Script>().r = Random.Range(0.0f, 1.0f);
            gO.GetComponent<DNA_Script>().g = Random.Range(0.0f, 1.0f);
            gO.GetComponent<DNA_Script>().b = Random.Range(0.0f, 1.0f);

            // add GameObject 
            population.Add(gO);

            
        }
    }

    GameObject Breed(GameObject parent1, GameObject parent2)
    {
        //position
        Vector3 pos = new Vector3(Random.Range(min, max), Random.Range(min, max), Random.Range(min, max));

        //offspring
        GameObject offspring = Instantiate(ObjInstantiate, pos, Quaternion.identity);

        // DNA Parent 1
        DNA_Script dna1 = parent1.GetComponent<DNA_Script>();
        // DNA Parent 2
        DNA_Script dna2 = parent2.GetComponent<DNA_Script>();

        // r
        float nR = dna1.r + dna2.r / 2;

        // g
        float nG = dna1.g + dna2.g / 2;

        // b
        float nB = dna1.b + dna2.b / 2;

        // rotation
        float nRot = dna1.RanRot + dna2.RanRot / 2;

        // aading the values we just created by mixing parents to offspring
        offspring.GetComponent<DNA_Script>().r = nR;
        offspring.GetComponent<DNA_Script>().g = nG;
        offspring.GetComponent<DNA_Script>().b = nB;
        offspring.GetComponent<DNA_Script>().RanRot = nRot;

        return offspring;
    }

    void BreedNewPopulation()
    {
        List<GameObject> newPopulation = new List<GameObject>();

        List<GameObject> sortedList = population.OrderBy(o => o.GetComponent<DNA_Script>().timeToDie).ToList();

        population.Clear();

        // breed upper half of sorted list
        for (int i = (int)(sortedList.Count / 2.0f) - 1; i < sortedList.Count - 1; i++)
        {
            population.Add(Breed(sortedList[i], sortedList[i + 1]));
            population.Add(Breed(sortedList[i + 1], sortedList[i]));
        }

        for (int i = 0; i < sortedList.Count; i++)
        {
            Destroy(sortedList[i]);
        }

        generation++;
    }

    // Update is called once per frame
    void Update()
    {
        elapsed += Time.deltaTime;
        if (elapsed > trialTime)
        {
            BreedNewPopulation();
            elapsed = 0;
        }
    }
}
