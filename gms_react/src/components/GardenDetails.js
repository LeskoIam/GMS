import {useState, useEffect} from 'react';
import Spinner from 'react-bootstrap/Spinner';
import Plant from "./Plant";
import {useParams} from "react-router-dom";
import Accordion from 'react-bootstrap/Accordion';
import Stack from "react-bootstrap/Stack";
import {Button} from "react-bootstrap";

const BASE_API_URL = "http://localhost:8000/api/";


export default function GardenDetails() {
  const params = useParams();
  const [garden_details, setGarden_details] = useState();

  useEffect(() => {
    (async () => {
      const response = await fetch(BASE_API_URL + 'garden/' + params.key);
      if (response.ok) {
        const results = await response.json();
        setGarden_details(results);
      } else {
        setGarden_details(null);
      }

    })();
  }, [params.key]);

  return (
    <>
      {garden_details === undefined ?
        <Spinner animation="border"/>
        :
        <>
          {garden_details === null ?
            <p>Could not retrieve &lt;Garden: '{params.key}'&gt; details.
              <br/><i>Probable cause: &lt;Garden: '{params.key}'&gt; does not exist</i>.</p>
            :
            <>
              <h1>{garden_details.name} {<Button variant="primary">Add Note to Garden</Button>}</h1>
              {garden_details.garden_beds.length === 0 ?
                <p>This garden has no garden beds added.</p>
                :
                <Accordion defaultActiveKey='0'>
                  {garden_details.garden_beds.map((bed, index) => (
                    <Accordion.Item key={index} eventKey={index.toString()}>
                      <Accordion.Header>
                        <Stack direction="horizontal" gap={3} className="GardenBedHeader">
                          <div className="p-2">{bed.name}<br/>{bed.description}</div>
                          <div className="p-2 ms-auto">{<Button variant="primary">Add Note to GardenBed</Button>}</div>
                        </Stack>
                      </Accordion.Header>
                      {bed.plants.length === 0 ?
                        <Accordion.Body>
                          <p>This garden bed has no plants added.</p>
                        </Accordion.Body>
                        :
                        <Accordion.Body>
                          <Stack direction="horizontal" gap={3} className="Plant">
                          {bed.plants.map((plant, i) => (
                            <Plant key={i} plant={plant}/>
                          ))}
                            </Stack>
                        </Accordion.Body>
                      }
                    </Accordion.Item>
                  ))}
                </Accordion>
              }
            </>
          }
        </>
      }
    </>
  );
}
