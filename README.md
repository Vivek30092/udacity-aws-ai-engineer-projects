<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Projects — Smart Budget Buddy & Intelligent Document Querying System</title>
</head>
<body>
  <h1>Udacity Generative AI Nanodegree — Project Showcase</h1>

  <p>
    This repository contains two capstone projects completed as part of the Udacity Generative AI with Large Language Models Nanodegree:
    <strong>Smart Budget Buddy</strong> (Project 1) and the <strong>Intelligent Document Querying System (IDQS)</strong> (Project 2).
    Both projects demonstrate agent/assistant design, responsible AI practices, and cloud-native retrieval & generation (RAG) architectures.
  </p>

  <hr />

  <h2>Project 1 — Smart Budget Buddy</h2>

  <h3>Overview</h3>
  <p>
    <em>Smart Budget Buddy</em> is an AI agent built to support a local school's financial literacy initiative for graduating students.
    The agent helps teens learn budgeting, saving, and basic financial concepts in a safe and age-appropriate manner.
  </p>

  <h3>Objective</h3>
  <ul>
    <li>Provide simple weekly/monthly budget guidance.</li>
    <li>Explain core financial terms (e.g., needs vs. wants, saving goals).</li>
    <li>Warn against common money traps (scams, impulse spending, unsafe lending).</li>
    <li>Be inclusive, safe, and suitable for teenage users.</li>
  </ul>

  <h3>Key Deliverables</h3>
  <ul>
    <li>Agent instructions (final prompt) for AWS Bedrock Agent Builder.</li>
    <li>Guardrails configuration to enforce safety and disallowed topics.</li>
    <li>Evaluation conversations (including edge-case tests).</li>
    <li>Screenshots demonstrating Agent Builder, Guardrails, and evaluations (included in project artifacts).</li>
  </ul>

  <h3>Features & Highlights</h3>
  <ul>
    <li>Design of agent tone and behavior for teen audiences (friendly, non-judgmental).</li>
    <li>Guardrails to avoid providing risky financial advice (no specific investment recommendations).</li>
    <li>Fallback guidance to trusted human resources (teachers, guardians) when outside scope.</li>
    <li>Iterative prompt engineering and testing against adversarial inputs.</li>
  </ul>

  <h3>Technologies & Concepts Demonstrated</h3>
  <ul>
    <li>AWS Bedrock Agent Builder</li>
    <li>Responsible AI / Guardrails</li>
    <li>Prompt engineering and agent evaluation</li>
  </ul>

  <hr />

  <h2>Project 2 — Intelligent Document Querying System (IDQS)</h2>

  <h3>Overview</h3>
  <p>
    The Intelligent Document Querying System implements an end-to-end retrieval-augmented generation (RAG) pipeline
    that allows domain-specific documents to be ingested, embedded, and queried for grounded responses using large
    foundation models.
  </p>

  <h3>Objective</h3>
  <ul>
    <li>Build a secure, scalable pipeline to ingest documents and answer queries using vector search and generation.</li>
    <li>Demonstrate infrastructure-as-code deployment and integration with AWS Bedrock Knowledge Base.</li>
  </ul>

  <h3>Key Deliverables</h3>
  <ul>
    <li>Terraform code to provision cloud infrastructure (VPC, Aurora Serverless, S3, etc.).</li>
    <li>pgvector-enabled Aurora Postgres for vector storage.</li>
    <li>Data ingestion and embedding pipeline (S3 → embeddings → vector store).</li>
    <li>Bedrock Knowledge Base integration and query/generation functions.</li>
    <li>Input validation, temperature & top_p controls, and basic error handling.</li>
  </ul>

  <h3>Features & Highlights</h3>
  <ul>
    <li>Full Infrastructure-as-Code (Terraform) deployment for reproducible environments.</li>
    <li>Secure secrets management using AWS Secrets Manager and least-privilege IAM (recommended).</li>
    <li>Vector search with pgvector for semantic retrieval of documents.</li>
    <li>RAG flows: retrieval of relevant passages + controlled generation.</li>
    <li>Implementation of robust input validation and response-generation functions.</li>
  </ul>

  <h3>Technologies & Concepts Demonstrated</h3>
  <ul>
    <li>AWS Bedrock Knowledge Base and Bedrock APIs</li>
    <li>Postgres + <code>pgvector</code> for vector storage</li>
    <li>Terraform for IaC (VPC, Aurora Serverless, S3)</li>
    <li>S3-based ingestion pipeline and embedding generation</li>
    <li>RAG architecture, prompt controls (temperature, top_p)</li>
  </ul>

  <hr />

 <h2>Reviewer Highlights</h2>
  <ul>
    <li><strong>Project 1:</strong> Praised for agent design, guardrails, and responsible AI practices for a teen audience.</li>
    <li><strong>Project 2:</strong> Recognized for complete Terraform deployment, secure configuration, pgvector integration, and correct Bedrock Knowledge Base integration.</li>
  </ul>

  <hr />

  <h2>Contact & Attribution</h2>
  <p>
    Project author: <strong>Vivek Kumar</strong><br />
    These projects were completed as part of the Udacity Generative AI with Large Language Models Nanodegree and the AWS AI &amp; ML scholarship curriculum.
  </p>
</body>
</html>
