import { createContext, useContext } from 'react';
import GmsApiClient from "../GmsApiClient";

const ApiContext = createContext();

export default function ApiProvider({ children }) {
  const api = new GmsApiClient();

  return (
    <ApiContext.Provider value={api}>
      {children}
    </ApiContext.Provider>
  );
}

export function useApi() {
  return useContext(ApiContext);
}