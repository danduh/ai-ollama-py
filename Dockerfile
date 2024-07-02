# Stage 1: Build Stage
FROM python:3.10-slim AS build

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
#RUN pip install --user --no-warn-script-location -r requirements.txt

# Copy the rest of the application code
COPY . .

# Stage 2: Production Stage
FROM python:3.10-slim AS production

# Set the working directory
WORKDIR /app

# Copy the dependencies from the build stage
COPY --from=build /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
#COPY --from=build /root/.local /root/.local
COPY --from=build /usr/local/bin /usr/local/bin
#COPY --from=build /usr/local/bin /usr/local/bin

# Copy the application code from the build stage
COPY --from=build /app /app

# Expose the port the app runs on
EXPOSE 8087

# Set environment variables (if needed)
ENV PYTHONUNBUFFERED=1

# Command to run the application
CMD ["python", "main.py"]
