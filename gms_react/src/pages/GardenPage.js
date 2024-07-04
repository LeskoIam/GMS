import Body from '../components/Body';
import {useParams} from "react-router-dom";

export default function GardenPage() {
  const { key } = useParams();

  return (
    <Body sidebar>
      <h1>{key}</h1>
      <p>TODO</p>
    </Body>
  );
}