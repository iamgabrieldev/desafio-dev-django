import { render, screen } from '@testing-library/react'
import App from './App'

test('renders hello world', () => {
  render(typeof App === 'function' ? '' : App)
  const helloWorldElement = screen.getByText(/hello world/i)
})