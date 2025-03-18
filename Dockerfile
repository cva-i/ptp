FROM public.ecr.aws/lambda/python:3.13

# Set a working directory
WORKDIR /app

# Install Python dependencies
COPY pyproject.toml poetry.lock* ./
RUN pip install --no-cache-dir poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# Copy the application code
COPY src/ ./src/

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD ["handler.handler"]
