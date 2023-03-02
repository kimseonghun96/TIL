일렉트론 빌드

```jsx
// public/electron.js
const { app, BrowserWindow } = require("electron");
const path = require("path");
const url = require("url");

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 900,
    height: 680,
    webPreferences: {
      nodeIntegration: true,
      enableRemoteModule: true,
      contextIsolation: false,
    },
  });

  if (process.env.NODE_ENV === "development") {
    mainWindow.loadURL(`http://localhost:3000`);
    mainWindow.webContents.openDevTools({ mode: "detach" });
  } else {
    mainWindow.loadURL(
      url.format({
        pathname: path.join(__dirname, "../build/index.html"),
        protocol: "file:",
        slashes: true,
      })
    );
  }

  mainWindow.on("closed", () => {
    mainWindow = null;
  });
}

app.on("ready", createWindow);

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") {
    app.quit();
  }
});

app.on("activate", () => {
  if (mainWindow === null) {
    createWindow();
  }
});
```

```jsx
// public/index.html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta
      name="description"
      content="Web site created using create-react-app"
    />
    <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
    <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
    <title>React Electron</title>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
    <script>
      const { ipcRenderer } = require("electron");
      const path = require("path");
      const url = require("url");
      const isDev = require("electron-is-dev");
      const root = document.getElementById("root");
      const startUrl = isDev
        ? "<http://localhost:3000>"
        : url.format({
            pathname: path.join(__dirname, "../build/index.html"),
            protocol: "file:",
            slashes: true,
          });
      ipcRenderer.on("navigate", (event, url) => {
        root.setAttribute("src", url);
      });
      root.setAttribute("src", startUrl);
    </script>
  </body>
</html>
```

```jsx
//src/App.tsx
import React from "react";
import logo from "./logo.svg";
import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="<https://reactjs.org>"
          target="_blank"
          rel="noopener noreferrer"
        >
          hihi
        </a>
      </header>
    </div>
  );
}

export default App;
```

```jsx
// src/index.tsx

import React from "react";
import ReactDOM from "react-dom";
import App from "./App";

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("root")
);
```

```jsx
// package.json
{
  "name": "testts",
  "version": "0.1.0",
  "description": "My test Electron app",
  "author": "My Name",
  "main": "public/electron.js",
  "dependencies": {
    "electron-is-dev": "^2.0.0"
  },
  "scripts": {
    "start": "electron .",
    "start:dev": "concurrently \\"npm start\\" \\"npm run react-start\\"",
    "react-start": "react-scripts start",
    "react-build": "react-scripts build",
    "build": "npm run react-build && electron-builder"
  },
  "homepage": "./",
  "build": {
    "appId": "com.example.testts",
    "productName": "TestTS",
    "directories": {
      "buildResources": "assets"
    }
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  },
  "devDependencies": {
    "concurrently": "^7.6.0",
    "cross-env": "^7.0.3",
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "electron": "^17.0.0",
    "electron-builder": "^22.11.7",
    "wait-on": "^7.0.1",
    "@types/electron": "^13.1.5"
  }
}
```

```jsx
// tsconfig.json
{
  "compilerOptions": {
    "target": "es5",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "module": "esnext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noImplicitAny": false,
    "noImplicitReturns": true,
    "noImplicitThis": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "jsx": "react",
    "sourceMap": true
  },
  "include": ["src"]
}
```
