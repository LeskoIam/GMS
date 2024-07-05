import Stack from 'react-bootstrap/Stack';
import Image from 'react-bootstrap/Image';
import { Link } from 'react-router-dom';

export default function Garden({ garden }) {
  return (
    <Stack direction="horizontal" gap={3} className="Garden">
      <Image src={'https://cdn.icon-icons.com/icons2/2070/PNG/128/garden_icon_125695.png'}
             alt="Garden image" roundedCircle />
      <div>
        <p>
          <Link to={'/garden/' + garden.pk}>
            {garden.name}
          </Link>
          &nbsp;&mdash;&nbsp;
          {garden.pk}:
        </p>
        <p>{garden.description}</p>
      </div>
    </Stack>
  );
}