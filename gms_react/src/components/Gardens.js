export default function Gardens() {
  const gardens = [
    {
      id: 1,
      name: 'Garden 1',
      description: "Garden description 1",
    },
    {
      id: 2,
      name: 'Garden 2',
      description: "Garden description 2",
    },

  ];
  return (
    <>
      {gardens.length === 0 ?
        <p>No gardens added.</p>
        :
        <ul>
          {gardens.map(garden => {
            return (
              <li key={garden.id}>
                <b>{garden.id}</b> &mdash; {garden.name} &mdash; {garden.description}
              </li>
            );
          })}
        </ul>
      }
    </>
  );
}
