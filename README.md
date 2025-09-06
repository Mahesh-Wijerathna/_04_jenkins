# Jenkins Hello World in Docker

This project sets up Jenkins using Docker Compose and includes a simple "Hello World" pipeline.

## Prerequisites
- Docker installed on your system
- Docker Compose installed

## Setup and Run
1. Navigate to the project directory:
   ```
   cd g:\7_SEM\ADVANCED AI\PROJECT\_04_jenkins
   ```

2. Start Jenkins:
   ```
   docker-compose up -d
   ```

3. Access Jenkins at http://localhost:8080

   Since Jenkins is already running and the volume is persisted, it should be accessible without setup. If you need to reset, run:
   ```
   docker-compose down -v
   ```
   Then start again to go through the initial setup.

## Creating the Hello World Job
1. In Jenkins, click "New Item"
2. Enter a name for your job (e.g., "HelloWorld")
3. Select "Pipeline" and click OK
4. In the Pipeline section, select "Pipeline script from SCM"
5. Choose "Git" as SCM (or copy the Jenkinsfile content directly)
6. For Git, enter the repository URL if you have one, or paste the Jenkinsfile content in the script box
7. Save and click "Build Now"

The pipeline will run and print "Hello World" in the console output.

## Stopping Jenkins
```
docker-compose down
```
