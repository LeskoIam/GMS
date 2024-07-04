import { useState, useEffect } from 'react';
import Spinner from 'react-bootstrap/Spinner';
import Garden from "./Garden";

const BASE_API_URL = "http://localhost:8000/api/";

export default function Gardens() {
  const [gardens, setGardens] = useState();

   useEffect(() => {
    (async () => {
      const response = await fetch(BASE_API_URL + 'gardens');
      if (response.ok) {
        const results = await response.json();
        setGardens(results);
      }
      else {
        setGardens(null);
      }
    })();
  }, []);

  return (
   <>
      {gardens === undefined ?
        <Spinner animation="border" />
      :
        <>
          {gardens === null ?
             <p>Could not retrieve blog posts.</p>
          :
            <>
              {gardens.length === 0 ?
                <p>There are no blog posts.</p>
              :
                gardens.map(garden => <Garden key={garden.pk} garden={garden} />)
              }
            </>
          }
        </>
      }
    </>
  );
}
