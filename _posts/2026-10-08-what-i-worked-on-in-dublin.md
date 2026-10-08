---
layout: post
title: "What I worked on in Dublin"
description: Building a web-based AI research assistant during my internship at NanobOx in Dublin.
---
I spent May 23 to August 15, 2026, interning at NanobOx in Dublin through World Endeavors. My supervisor was [Dr. Mohammad Reza Ghaani](https://www.nanobox.ie/about), who also worked at Trinity College Dublin. I worked at the NanobOx building.

NanobOx develops nanobubble technology, which creates tiny gas bubbles in water. The company's [website](https://www.nanobox.ie/) describes applications in agriculture, aquaculture, and industry. My job was to build a web-based AI assistant that could answer questions using documents about nanobubbles.

## Starting with an idea

When I arrived, there was an idea and a small set of requirements. I built the application myself and made the implementation decisions. The original request was fairly simple: give people a way to ask questions about the documents through a web interface.

The purpose was to make research easier to search and understand. Scientific information is spread across papers, and finding the relevant information can take time. The assistant needed to find useful material in those documents and use it to answer a question with sources.

## How the assistant worked

The application used a process called retrieval-augmented generation, or RAG. It processed documents into smaller sections and stored representations of those sections so it could search for relevant information. When someone asked a question, it retrieved matching material and supplied that context to an AI model to help it write an answer.

Python handled the backend work, and React provided the web interface. Ollama ran local AI models, while ChromaDB stored the document representations used for retrieval.

One design choice was to run the main AI models locally. That kept the core model processing on the project's server. The system still used online sources to discover literature, so locally hosted did not mean the entire application was disconnected from the internet.

## Making it work in practice

I worked on document ingestion, getting answers to stream into the browser, and configuring the models. Document ingestion made the papers searchable, while streaming let answers appear in the browser as they were generated.

Python was familiar to me. The newer parts were working with Ubuntu Server and the AI tools. I had to learn how to put the pieces together and run them as an application on a server.

By the end of the internship, I had tested, demonstrated, deployed, and handed over the platform. Dr. Ghaani liked my work.

The internship taught me more about how I work and how important feedback is when building something for someone else. It also gave me a clearer view of what I could do in the field.
