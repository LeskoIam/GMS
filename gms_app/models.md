```mermaid
erDiagram
    Garden {
        string name
        string description
    }
    GardenBed {
        garden Garden FK
        string name
        string description
    }
    Plant {
        gardenbed GardenBed FK
        string name
        string description
    }
    PlantPreset {
        string name
        string description
    }

    Garden ||--|{ GardenBed: ""
    GardenBed }|--|{ Plant: ""
```