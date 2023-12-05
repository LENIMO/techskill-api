import express from 'express'
import fs from 'fs/promises'

const app = express()
const PORT = process.env.PORT || 3000
const jsonFilePath = './techstack_names.json'

async function readJsonFile() {
  try {
    const jsonData = await fs.readFile(jsonFilePath, 'utf-8')
    return JSON.parse(jsonData)
  } catch (error) {
    console.error('Error reading JSON file:', error.message)
    return null
  }
}

app.get('/api/techstacks', async (req, res) => {
  const techstackNames = await readJsonFile()
  if (techstackNames) {
    res.json(techstackNames)
  } else {
    res.status(500).json({ error: 'Internal Server Error' })
  }
})

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`)
})
