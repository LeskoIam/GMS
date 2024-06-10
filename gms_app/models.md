```mermaid
erDiagram
    Garden {
        string name
        string description
    }
    GardenBed {
        Garden garden FK
        string name
        string description
    }
    Plant {
        string name
        string description
        garden_bed GardenBed FK
    }
    Planting {
        Plant plant FK
        GardenBed gardenBed FK
        json location
    }
    PlantPreset {
        string name
        string description
    }

    Garden ||--o{ GardenBed: ""
    GardenBed }|--o{ Planting: ""
    Planting }|--o{ Plant: ""
```