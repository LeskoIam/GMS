import Body from '../components/Body';

export default function AboutPage() {
  return (
    <Body sidebar>
      <h1>About</h1>
      <p>
        <h3>Developers:</h3>
        <div>
          <p>Matevž Polenšek <a href={"https://github.com/LeskoIam"}>GitHub</a></p>
          <p>johnbaldwin <a href={"https://github.com/johnbaldwin"}>GitHub</a></p>
        </div>
      </p>
    </Body>
  );
}