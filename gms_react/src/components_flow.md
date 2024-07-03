```mermaid
flowchart

App["App.js"]

Head["components/Header.js"]
Body["components/Body.js"]
Gardens["components/Gardens.js"]
Sidebar["components/Sidebar.js"]


GardenPage["pages/GardenPage.js"]
AboutPage["pages/AboutPage.js"]
LoginPage["pages/LoginPage.js"]

App --> Head
App --> GardenPage
App --> AboutPage
App --> LoginPage

GardenPage --> Body --> Sidebar
Body --> Gardens

AboutPage --> Body

LoginPage --> Body

```