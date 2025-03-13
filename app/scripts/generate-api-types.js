// This script generates TypeScript types from your FastAPI OpenAPI schema
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { dirname } from 'path';
import { execSync } from 'child_process';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

async function generateTypes() {
  try {
    // Fetch the OpenAPI schema
    const response = await fetch(
      'https://where-is-my-money-api.vercel.app/openapi.json'
    );

    if (!response.ok) {
      throw new Error(`Failed to fetch schema: ${response.statusText}`);
    }

    const schema = await response.json();

    // Save the schema to a file
    const schemaPath = path.join(__dirname, '../app/openapi.json');
    fs.writeFileSync(schemaPath, JSON.stringify(schema, null, 2));

    console.log('OpenAPI schema saved to app/openapi.json');

    // Generate TypeScript types using openapi-typescript
    try {
      execSync(
        `npx openapi-typescript ${schemaPath} --output app/types/api.ts`
      );
      console.log(
        'TypeScript types generated successfully in app/types/api.ts'
      );
    } catch (error) {
      console.error('Failed to generate TypeScript types:', error.message);
    }
  } catch (error) {
    console.error('Error generating API types:', error.message);
  }
}

generateTypes();
