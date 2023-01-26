import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import '@/styles/global.css'
import '@/index.css'
import App from '@/app/App'

const container = document.getElementById('root') as HTMLDivElement

createRoot(container).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
