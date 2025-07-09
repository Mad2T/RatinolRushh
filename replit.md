# Rational Function Quest - Educational Math Game

## Overview

This is a full-stack educational math game built with React, Express, and TypeScript. The game challenges players to identify characteristics of rational functions (vertical asymptotes, horizontal asymptotes, holes, and intercepts) by selecting the correct graph from multiple choice options. The application features a Mario-inspired design with a leaderboard system to track player performance.

## User Preferences

Preferred communication style: Simple, everyday language.
Game Design: Nintendo-style retro gaming aesthetics with 5-level progression system.

## System Architecture

### Frontend Architecture
- **Framework**: React with TypeScript
- **UI Library**: Radix UI components with shadcn/ui styling
- **Styling**: Tailwind CSS with custom Mario-themed colors and fonts
- **State Management**: React hooks with local component state
- **Data Fetching**: TanStack Query (React Query) for API communication
- **Routing**: Wouter for client-side routing
- **Build Tool**: Vite for development and production builds

### Backend Architecture
- **Framework**: Express.js with TypeScript
- **API Design**: RESTful endpoints for leaderboard and player data
- **Database**: PostgreSQL with Drizzle ORM
- **Validation**: Zod for schema validation
- **Session Management**: Express sessions with PostgreSQL storage
- **Development Server**: Hot reload with Vite middleware integration

### Database Schema
The application uses a single `players` table with the following structure:
- `id`: Primary key (serial)
- `name`: Player name (text)
- `score`: Final game score (integer)
- `accuracy`: Percentage accuracy (integer)
- `questionsAnswered`: Total questions answered (integer)
- `correctAnswers`: Number of correct answers (integer)
- `timeCompleted`: Time taken to complete game in seconds (integer)
- `createdAt`: Timestamp of record creation

## Key Components

### Game Engine
- **RationalFunction**: Core data structure containing function expressions and graph characteristics
- **GameLogic**: Scoring system, hint generation, and answer validation
- **MathUtils**: Function generation and graph rendering utilities
- **GameCanvas**: HTML5 Canvas component for rendering mathematical graphs

### User Interface
- **GameHeader**: Displays level, score, and timer
- **FunctionDisplay**: Shows the current rational function to analyze
- **GraphChoices**: Multiple choice graph selection interface
- **GameStatus**: Player statistics and hints display
- **Leaderboard**: Top player rankings
- **GameModals**: Name input and game over screens

### Storage Layer
- **MemStorage**: In-memory storage implementation for development
- **IStorage**: Interface for storage operations (get/create players, leaderboard)
- **Drizzle ORM**: Database abstraction layer with PostgreSQL support

## Data Flow

1. **Game Initialization**: Player enters name → Game state initialized with 90 seconds, 15 questions
2. **Level Progression**: 5 levels (Beginner → Apprentice → Skilled → Expert → Master)
3. **Question Generation**: Math utilities generate level-appropriate rational function with correct answer
4. **Player Interaction**: Player selects graph option → Answer validation
5. **Score Calculation**: Based on correctness, time remaining, level multiplier, and perfect bonuses
6. **Game Completion**: Final score submitted to database → Leaderboard updated
7. **Leaderboard Display**: Top players fetched and displayed with Nintendo-style rankings

## External Dependencies

### Frontend Dependencies
- **React Ecosystem**: React, React DOM, React Query for data fetching
- **UI Components**: Radix UI primitives, Lucide React icons
- **Styling**: Tailwind CSS, class-variance-authority for component variants
- **Utilities**: date-fns for date formatting, clsx for conditional classes

### Backend Dependencies
- **Server**: Express.js with TypeScript support
- **Database**: Drizzle ORM with PostgreSQL driver (@neondatabase/serverless)
- **Validation**: Zod for runtime type checking
- **Session**: connect-pg-simple for PostgreSQL session storage

### Development Tools
- **Build**: Vite with React plugin and TypeScript support
- **Database**: Drizzle Kit for migrations and schema management
- **Runtime**: tsx for TypeScript execution in development

## Deployment Strategy

### Build Process
1. **Frontend Build**: Vite builds React app to `dist/public`
2. **Backend Build**: esbuild bundles server code to `dist/index.js`
3. **Database Setup**: Drizzle migrations run against PostgreSQL instance

### Production Configuration
- **Environment**: Node.js production environment
- **Database**: PostgreSQL connection via DATABASE_URL environment variable
- **Static Files**: Express serves built React app from `dist/public`
- **API Routes**: Express handles `/api/*` endpoints

### Development Workflow
- **Hot Reload**: Vite dev server with Express middleware integration
- **Type Checking**: TypeScript compilation with strict mode enabled
- **Database**: Drizzle push for schema synchronization during development

### Key Architectural Decisions

1. **Monorepo Structure**: Frontend (`client/`), backend (`server/`), and shared code (`shared/`) in single repository for easier development and type sharing

2. **In-Memory Storage**: Development uses MemStorage class for rapid prototyping, easily replaceable with database implementation

3. **Shared Schema**: Drizzle schema and Zod validation shared between frontend and backend for type safety

4. **Canvas Rendering**: HTML5 Canvas for mathematical graph rendering provides precise control over graph visualization

5. **Component-Based UI**: Modular React components with shadcn/ui for consistent styling and accessibility

6. **API-First Design**: Clean separation between frontend and backend with RESTful API endpoints

This architecture supports rapid development while maintaining scalability and type safety throughout the application.

## Recent Changes (January 2025)

### Enhanced Nintendo-Style Gaming Experience
- ✓ Implemented 5-level progression system (Beginner → Apprentice → Skilled → Expert → Master)
- ✓ Added level-specific rational function complexity and difficulty scaling
- ✓ Enhanced visual design with Nintendo-style cards, animations, and effects
- ✓ Improved scoring system with time bonuses, level multipliers, and perfect bonuses
- ✓ Added level-specific hints with emojis and gaming terminology
- ✓ Enhanced game header with dynamic level indicators and crown effects
- ✓ Improved leaderboard with rank-based icons and Nintendo-style visual hierarchy
- ✓ Updated game modals with level progression display and score ranking system
- ✓ Added pulsing, glowing, and coin-spinning animations for enhanced visual appeal
- ✓ Extended game duration to 90 seconds with 15 questions for better progression

### Level System Details
- **Level 1 (Beginner)**: Basic linear over linear functions
- **Level 2 (Apprentice)**: Functions with removable discontinuities (holes)
- **Level 3 (Skilled)**: Linear over quadratic with multiple asymptotes
- **Level 4 (Expert)**: Quadratic over quadratic functions
- **Level 5 (Master)**: Complex functions with multiple features

This creates an engaging, progressive learning experience that maintains educational value while incorporating retro gaming aesthetics.