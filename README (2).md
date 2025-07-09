# Rational Function Quest

A Nintendo-style educational math game for learning rational function graphing with interactive gameplay and leaderboard tracking.

## Features

- 5 progressive difficulty levels (Beginner → Apprentice → Skilled → Expert → Master)
- Interactive graph identification gameplay
- Real-time scoring with time bonuses and level multipliers
- Nintendo-style retro design with animations
- Leaderboard system with player rankings
- Educational hints and feedback

## Technologies Used

- **Frontend**: React, TypeScript, Tailwind CSS, Vite
- **Backend**: Express.js, Node.js
- **Database**: PostgreSQL with Drizzle ORM
- **UI Components**: Radix UI with shadcn/ui

## Local Development

1. Install dependencies:
   ```bash
   npm install
   ```

2. Start the development server:
   ```bash
   npm run dev
   ```

3. Open your browser to `http://localhost:5000`

## Deployment

### Option 1: Deploy to Vercel (Frontend + Backend)

1. Fork this repository
2. Connect your GitHub repo to Vercel
3. Set the build command to `npm run build`
4. Set the output directory to `dist/public`
5. Add environment variables for your database

### Option 2: Deploy to Railway

1. Fork this repository
2. Connect your GitHub repo to Railway
3. Railway will automatically detect the Node.js app and deploy

### Option 3: Deploy to Render

1. Fork this repository
2. Connect your GitHub repo to Render
3. Set the build command to `npm run build`
4. Set the start command to `npm start`

## Environment Variables

For production deployment, you'll need to set up:

- `DATABASE_URL` - PostgreSQL connection string
- `NODE_ENV` - Set to "production"

## Game Structure

The game progresses through 5 levels:
1. **Beginner**: Basic linear over linear functions
2. **Apprentice**: Functions with holes (removable discontinuities)
3. **Skilled**: Linear over quadratic with multiple asymptotes
4. **Expert**: Quadratic over quadratic functions
5. **Master**: Complex functions with multiple features

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License