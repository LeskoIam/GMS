import Stack from 'react-bootstrap/Stack';
import Image from 'react-bootstrap/Image';
import {Link} from 'react-router-dom';
import {Card} from "react-bootstrap";
import {Button} from "react-bootstrap";

// export default function Plant({plant}) {
//   return (
//     <Stack direction="horizontal" gap={3} className="Plant">
//       <Image src={'https://cdn.icon-icons.com/icons2/733/PNG/64/plant_icon-icons.com_63010.png'}
//              alt="Garden image" roundedCircle/>
//
//       <div>
//         <Link to={'/plant/' + plant.pk}>
//           {plant.name}
//         </Link>
//         &nbsp;&mdash;&nbsp;
//         {plant.pk}:
//       </div>
//       <div>
//         <p>{plant.description}</p>
//       </div>
//     </Stack>
//   );
// }

export default function Plant({plant}) {
  return (

    <div>
      <Card style={{width: '14rem'}}>
        <Card.Img variant="top" src="https://cdn.icon-icons.com/icons2/733/PNG/128/plant_icon-icons.com_63010.png"/>
        <Card.Body>
          <Card.Title>{plant.name}</Card.Title>
          <Card.Text>

            <p>{plant.description}</p>
            <p>{plant.location}</p>
          </Card.Text>
          <Button variant="primary">Add Note to Plant or Planting</Button>
        </Card.Body>
      </Card>
    </div>

  );
}