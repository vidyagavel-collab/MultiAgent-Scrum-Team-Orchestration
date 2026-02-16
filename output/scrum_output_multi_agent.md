
            ⏱ Total runtime: 1.07 minutes
            ---
            # 📋 Scrum AI Team Deliverables

## None
I want to build an AI driven app to classify the PDF which are currently done manually.

## None
Transferred to ProductOwner

## ProductOwner
Epic ID: E001  
Epic Title: Create an AI Model to Classify PDFs Automatically  
Business Objective: Replace manual PDF classification with AI to improve speed, reduce human error, and optimize resource utilization in processing documents.  
Business Value Score (1–10): 9  
Effort Estimate: High  
Priority Rank: 1  

---

Epic ID: E002  
Epic Title: Develop a User-Friendly Interface for PDF Uploads and Classification Results  
Business Objective: Allow users to upload PDFs easily and view confidently classified results, ensuring seamless interaction with the AI-driven classification system.  
Business Value Score (1–10): 8  
Effort Estimate: Medium  
Priority Rank: 2  

---

Epic ID: E003  
Epic Title: Implement Data Preprocessing Mechanism for PDFs  
Business Objective: Ensure consistent and high-quality input by cleaning, parsing, and structuring PDF data before feeding it to the AI model for accurate classification.  
Business Value Score (1–10): 7  
Effort Estimate: Medium  
Priority Rank: 3  

---

Epic ID: E004  
Epic Title: Enable Reporting and Analytics on Classification Outcomes  
Business Objective: Provide stakeholders with valuable insights into classified PDFs via reports and analytics, enhancing decision-making and tracking performance.  
Business Value Score (1–10): 6  
Effort Estimate: Medium  
Priority Rank: 4  

---

Epic ID: E005  
Epic Title: Build Data Annotation and Feedback Loop for Improving AI Accuracy  
Business Objective: Incorporate a feedback system for users to correct misclassifications and continuously train the AI, ensuring higher accuracy over time.  
Business Value Score (1–10): 6  
Effort Estimate: High  
Priority Rank: 5  

---

### Prioritization Explanation:  
The first epic (E001) represents the foundation for the AI-driven solution and is critical to achieving the primary business objective, warranting the highest rank despite the high effort. User accessibility (E002) is ranked second and is necessary to bridge end users and the AI system, providing high value with moderate difficulty. Data preprocessing (E003) supports the model's accuracy; hence, it follows close behind. Reporting (E004) and improvement mechanisms (E005) have a relatively lower immediate value and are ranked lower but are still essential for the long-term success of the app.

## None
Transferred to BusinessAnalyst

## BusinessAnalyst
### Breaking Down Into User Stories:
Let’s focus on building the AI-driven application to classify PDFs. I’ll break down the initial epic “**E001: Create an AI Model to Classify PDFs Automatically**” into clear, precise Agile user stories suited for the team.

#### **Story 1: Upload and Extract PDF Content**  
As a **system**,  
I want to **extract text and metadata from uploaded PDFs**,  
So that **the content can be analyzed for classification**.

**Functional Requirements:**
- The system must accept PDF files up to 50MB in size.
- Extract plain text content from the PDF (including OCR for scanned PDFs).
- Extract metadata such as the document title, author, created date, and page count.
- Notify users if the PDF extraction fails.

**Non-Functional Requirements:**
- PDFs should be processed within 5 seconds each for extraction.
- Support PDFs with multilingual text, preferably UTF-8.

**Acceptance Criteria:**
- **Given** the user has uploaded a valid PDF file,  
  **When** the processing completes,  
  **Then** the extracted content and metadata should be stored in the system.  

- **Given** the user uploads an invalid or unreadable PDF (e.g., corrupted file),  
  **When** the system tries to extract content,  
  **Then** the user should see an error message "Unable to process this document. Please try again or upload a valid PDF."

**Edge Cases:**
- PDF with no text content (images-only formats).
- Large files that exceed system limits.
- Password-protected PDFs.

---

#### **Story 2: Classify Extracted Content Using AI Model**  
As a **system**,  
I want to **classify extracted content using the AI model**,  
So that **it determines the category of the document accurately**.

**Functional Requirements:**
- The classification model must assign one of the defined categories to each PDF (e.g., "Invoice," "Contract," "Report").
- Allow custom categories that can be added dynamically via configuration.

**Non-Functional Requirements:**
- Classification must operate at 80% or higher confidence for each category. For AI outputs below confidence, it should suggest "Uncertain" with reasoning.
- The process must take less than 3 seconds for documents of up to 20 pages.

**Acceptance Criteria:**
- **Given** extracted content from a valid PDF,  
  **When** the AI model processes the textual data,  
  **Then** it should assign the appropriate classification label (e.g., "Invoice").  

- **Given** the AI is not confident about its classification (below a set threshold),  
  **When** the system tries to classify it,  
  **Then** it should mark the document as “Uncertain” and record the classification confidence score for users to review.

**Edge Cases:**
- Content that matches multiple categories equally (e.g., 50% confidence for two).
- PDFs with no text (e.g., blank documents or heavily damaged ones).

---

#### **Story 3: Allow Re-Training of the AI Model Based on New Data**  
As a **business analyst**,  
I want to **upload labeled datasets**,  
So that **the AI model can be retrained to improve accuracy**.

**Functional Requirements:**
- Accept CSV/JSON files containing document content along with the corresponding category label.
- Trigger an AI retraining process and update the classification model with new data.

**Non-Functional Requirements:**
- Retraining duration must not exceed 30 minutes for datasets of 10,000 documents.
- Maintain existing model performance metrics (e.g., F1 score must not degrade by more than 1%).

**Acceptance Criteria:**
- **Given** a properly formatted labeled dataset,  
  **When** the system completes retraining,  
  **Then** the AI classification model accuracy should improve based on test results.

- **Given** an improperly formatted dataset,  
  **When** the user uploads it,  
  **Then** the system should reject the dataset and display an error message explaining the rejection.

**Edge Cases:**
- If the added data introduces bias or degrades the model’s accuracy significantly (e.g., overfitting to specific patterns).
- Retraining failure due to system resource limitations (e.g., exceeding memory or CPU).

---

#### **Story 4: Monitor and Log Classification Results**  
As a **business user**,  
I want to **view logs of classification performance**,  
So that **I can monitor the accuracy and efficiency of the PDF classification system**.

**Functional Requirements:**
- Store each PDF's classification label, confidence score, processing time, and status.
- Provide a dashboard to query logs by date range, file type, or category.

**Non-Functional Requirements:**
- Logs must be searchable within 2 seconds.
- Ensure log storage maintains compliance with GDPR, retaining only necessary classification data.

**Acceptance Criteria:**
- **Given** classification logs for successfully processed documents,  
  **When** the user queries by a specific date range,  
  **Then** all logs within that range should be displayed with confidence levels.

- **Given** confidential PDFs processed by the system,  
  **When** logs are queried,  
  **Then** sensitive content should not be displayed but anonymized or hidden as per privacy rules.

**Edge Cases:**
- Logs for failed classifications with no associated confidence score or category.
- Large amounts of logs being queried (pagination required).

---

This breakdown focuses only on the **E001: AI Model and Classification Workflow**. Once this is implemented, we can build out functionality for UI, analytics, and feedback loops in subsequent sprints or iterations. Each story is ready for development.

## None
Transferred to SolutionArchitect

## SolutionArchitect
### High-Level Solution Architecture for the AI-Driven PDF Classification App

#### **Overview of Major Components**
1. **Frontend Interface (Web/Mobile App)**:  
   A user-facing interface where users can upload PDFs, view results, track classification progress, and provide feedback.  
   - **Features**: File upload functionality, results display, feedback mechanism.
   - **Technology Options**: React.js, Angular for web; React Native, Flutter for mobile.  

2. **Backend Services (API Layer)**:  
   Handles requests from the frontend, orchestrates data flow, and interacts with various backend services.  
   - **Features**: API gateways, authentication, PDF upload management, and responses to AI classifications.
   - **Technology Options**: Node.js/Django/Spring Boot for scalable REST API services.  

3. **Data Preprocessing Module**:  
   Extracts text and metadata from PDFs and prepares them for classification.  
   - **Features**:  
     - Extracts text using tools like Apache Tika or PyPDF2 for textual PDFs.  
     - Optical Character Recognition (OCR) for scanned PDFs using Tesseract or Google Cloud Vision API.  
   - **Technology Options**: Python libraries or microservices designed for preprocessing PDFs.

4. **AI/ML Classification System**:  
   Core module where PDFs are classified using an AI-based model.  
   - **ML Frameworks**: TensorFlow, PyTorch, or Scikit-Learn.  
   - **Key Models**: Fine-tuned transformer-based models like BERT, RoBERTa, or custom models tailored for document classification.

5. **File Storage**:  
   Stores uploaded PDFs and associated classification results.  
   - **Options**: Cloud storage such as AWS S3 buckets, Azure Blob Storage, or Google Cloud Storage.  

6. **Database**:  
   Data persistence layer to store document metadata, user feedback, classification logs, and performance metrics.  
   - **Options**: Relational DB (PostgreSQL/MySQL) for structured metadata and NoSQL DB (MongoDB) for logs or unstructured feedback data.  

7. **Feedback and Re-Training Module**:  
   Mechanism to incorporate user feedback for improving AI performance and building a dynamic learning mechanism.  
   - Allows users to correct the AI classification and label data.   
   - Automates periodic re-training cycles to improve accuracy.  
   - **Tools**: Streamlit dashboards or custom tools in Django/Flask for labeling and retraining workflows.  

8. **Analytics and Reporting Dashboard**:  
   Provides insights into system performance (e.g., confidence scores, processing times) and breakdown of classifications and errors.  

9. **Deployment Environment**:  
   Handles deployment, scalability, security, and monitoring.  
   - **Application Hosting**: AWS, GCP, or Microsoft Azure.  
   - **CI/CD Tools**: Jenkins, GitHub Actions, or GitLab CI/CD.  
   - **Containerization & Orchestration**: Docker and Kubernetes services for scalability and microservices management.  
   - Use APM tools like Datadog or AWS CloudWatch for system monitoring.  

---

#### **System Interactions**
1. **User Interaction**  
    - Users upload PDFs through the frontend, triggering the backend services.  
    - Progress is shown in real-time, and results of classification are displayed upon completion.

2. **Backend Processing**  
    - File upload triggers the Data Preprocessing module to extract text and metadata.  
    - Extracted data is passed to the AI/ML Classification System and results are returned (e.g., category, confidence score).  

3. **System Logging and Analytics**  
    - Results are stored in the database alongside metadata.  
    - Logs and metrics are available via the Reporting Dashboard.

4. **Feedback Loop**  
    - User feedback is captured and logged for false positives/false negatives.  
    - Feedback data is used for periodic re-training of the AI model.  

5. **Storage and Retrieval**  
    - PDFs and associated metadata/results are stored in a file storage system and database.
    - End-users can retrieve results for any file uploaded in the past.  

---

### High-Level Infrastructure Needs  

| Component                  | Solution                             | Services/Tools                                           |
|----------------------------|--------------------------------------|---------------------------------------------------------|
| **Frontend Hosting**       | Cloud-based Web App Frontend        | AWS Amplify, Azure App Service, Vercel, or Firebase.    |
| **API/Backend Services**   | Scalable Backend                    | AWS Lambda, API Gateway, GCP Cloud Functions.           |
| **Document Processing**    | Text Extraction and OCR             | Tesseract, Google Cloud Vision, Apache Tika.            |
| **AI/ML Model Hosting**    | Managed ML Services                 | AWS SageMaker, GCP AI Platform, TensorFlow Serving.     |
| **Storage**                | File Storage and Database Hosting   | AWS S3, Azure Blob, MongoDB Atlas, PostgreSQL RDS.      |
| **Retraining and Feedback**| Managed ML Pipelines for Feedback   | Kubeflow Pipelines (GCP), Vertex AI, MLFlow.            |
| **Monitoring and Logging** | DevOps and Observability            | Datadog, New Relic, AWS CloudWatch, ELK Stack.          |

---

### Technical Dependencies
1. **Document Processing Tools**: Dependence on tools like Tesseract (OCR) or libraries capable of extracting metadata from complicated PDFs.  
2. **Model Training Data**: High-quality annotated datasets for training the model on domain-specific PDFs.  
3. **Cloud Infrastructure**: Subscription/usage of cloud services (AWS/GCP/Azure) for storage, AI hosting, and scalability.  
4. **Security Compliance**: GDPR/HIPAA compliance may require architecture alignment with regulations to secure sensitive PDF uploads.  

---

### Risks 
1. **Model Performance**:  
   - AI classification accuracy might not meet business needs initially.
   - Risk of "Uncertain" classifications causing frustration.  
   **Mitigation**: Use a pre-trained NLP model and fine-tune it on labeled data with an active feedback mechanism.

2. **Processing Delays**:  
   - Large PDFs or documents with heavy images could lead to processing delays.  
   **Mitigation**: Introduce job queues for background processing and optimize OCR tools.  

3. **Scalability Constraints**:  
   - Processing large-scale PDF uploads during peak times may overwhelm infrastructure.  
   **Mitigation**: Leverage serverless architecture for auto-scaling (e.g., AWS Lambda or GCP Cloud Run).

4. **Data Privacy and Security**:  
   - Risk in handling sensitive PDFs (e.g., contracts or financial records).  
   **Mitigation**: Ensure uploaded PDFs are encrypted at rest (AWS KMS/Azure Key Vault) and allow configurable retention policies.

---

### Suggested New Technical User Stories  
1. **Error Handling for Invalid Files**: Build mechanisms to notify users about corrupted or invalid PDFs during preprocessing.  
2. **Bulk PDF Upload Support**: Enable users to upload multiple PDFs at once, with background queuing for processing.  
3. **Customizable Category Definition**: Allow admins to add/remove categories dynamically to keep the classification system flexible.  
4. **Confidence Threshold Management**: Provide settings to tune confidence thresholds where classifications are marked "Uncertain."  
5. **On-Premise Deployment Option**: Allow businesses with specific compliance needs to deploy the system on private infrastructure instead.

---

This architecture and set of dependencies will enable the team to implement a robust first version of the AI-driven PDF classifier with scalability and improvement pathways for further iterations.

## None
Transferred to QATester

## QATester
### Test Scenarios and Test Cases in Gherkin Syntax
Below are comprehensive test scenarios and test cases for the foundational functionality related to building the AI-driven PDF classifier. These will cover upload, extraction, AI classification, feedback/retraining, and overall process verification.

---

#### **Feature: PDF Upload and Extraction**
**Scenario: Successful PDF upload and extraction of text and metadata**  
```
Given the user uploads a valid PDF file  
When the system attempts to extract text and metadata from the file  
Then the system successfully extracts text and metadata  
And stores the extracted data for further processing  
```

**Scenario: User uploads an invalid or corrupted PDF**  
```
Given the user uploads an invalid PDF file  
When the system attempts to process the file  
Then the system must fail and produce an error message "Unable to process this document. Please try again or upload a valid PDF"  
```

**Scenario: Uploaded PDF exceeds the size limit**  
```
Given the user uploads a PDF larger than 50MB  
When the system validates the file size  
Then the upload should fail with an error "File size exceeds the allowed limit of 50MB"  
```

**Scenario: PDFs without textual content (images-only format)**  
```
Given the user uploads a PDF containing only images without text  
And optical character recognition (OCR) is enabled in the preprocessing module  
When the system processes the file  
Then OCR should extract text from the images successfully  
And metadata should be extracted and stored  
```

**Scenario: Password-protected PDF file upload**  
```
Given the user uploads a password-protected PDF file  
When the system attempts to process the file  
Then the system must fail and produce an error stating "Unable to process password-protected files. Please remove the password and try again"  
```

---

#### **Feature: AI Classification of Extracted Content**
**Scenario: Accurate classification based on extracted content**  
```
Given the extracted content from a valid PDF  
When the AI classification system receives the processed data  
Then the system assigns the appropriate classification label (e.g., "Invoice")  
And stores the category along with the confidence score  
```

**Scenario: Classification returns "Uncertain" due to low confidence**  
```
Given the extracted content from a valid PDF  
And the document matches multiple categories at low confidence levels  
When the AI system processes the data  
Then the system marks the classification result as "Uncertain"  
And records the confidence score for user review  
```

**Scenario: Classification fails due to insufficient AI training data**  
```
Given the AI classification system has been trained on limited document categories  
When the extracted content's distribution does not match predefined categories  
Then the system fails to classify the document  
And produces an error message stating "Document category not recognized"  
```

**Scenario: Custom category integration for classification**  
```
Given an admin adds a new category "Legal Agreement" to the classification system  
And the system retrains the AI model to include this new category  
When a user uploads a PDF matching the "Legal Agreement" type  
Then the system should classify the document correctly as "Legal Agreement"  
```

---

#### **Feature: Feedback System for Misclassification**
**Scenario: User provides feedback to correct a misclassified document**  
```
Given the AI system assigns an incorrect classification label to a document  
When the user overrides the classification  
And assigns the correct category "Report"  
Then the system records the user feedback  
And stores the corrected category for future use  
```

**Scenario: Bulk feedback for retraining purposes**  
```
Given the user uploads multiple labeled corrections via a CSV file  
When the system processes the uploaded feedback file  
Then the AI system records the newly labeled classifications  
And prepares to retrain the model using these corrections  
```

**Scenario: Invalid feedback upload format**  
```
Given the user uploads an improperly formatted feedback file  
When the system validates the file  
Then the system rejects the file with an error message "Invalid format. Please upload a properly formatted JSON or CSV file"  
```

---

#### **Feature: Analytics and Reporting**
**Scenario: Querying classification results by date range**  
```
Given the system has stored classification logs for several documents  
When the user queries logs for a specific date range  
Then the system retrieves and displays classification results for that date range  
```

**Scenario: Handling sensitive metadata in logs under GDPR compliance**  
```
Given the system stores classification metadata for PDFs  
And the metadata contains sensitive user information  
When the user queries the logs  
Then the system anonymizes or hides sensitive information in compliance with GDPR regulations  
```

**Scenario: Pagination for large log data queries**  
```
Given the system contains a large number of classification logs  
When the user queries logs without a defined page size  
Then the system paginates the logs automatically to ensure manageable data viewing  
```

---

#### **Feature: Model Re-Training Workflow**
**Scenario: Successful retraining of the AI model using labeled dataset**  
```
Given the user uploads a valid labeled dataset for retraining  
When the system validates and processes the dataset  
Then the system retrains the AI classification model successfully  
And updates its categorized accuracy on new test cases  
```

**Scenario: Retraining failure due to limited system resources**  
```
Given the AI system starts retraining with a labeled dataset  
And the system's available resources are insufficient for processing the data  
When the retraining process is initiated  
Then the system halts and records an error message "Retraining failed due to resource limitations"  
```

---

#### **Feature: Scalability and Performance**
**Scenario: Bulk upload of multiple PDFs**  
```
Given the user uploads a batch of multiple PDFs for processing  
When the system starts processing the files  
Then the system processes each file asynchronously  
And returns classification results for all files once processing is complete  
```

**Scenario: Processing large PDFs within time limits**  
```
Given the user uploads a valid large PDF file under the size limit (e.g., 50MB)  
When the system processes the file  
Then the text extraction and classification should complete within 5 seconds  
```

---

### Conclusion
These test cases should comprehensively validate the functionality, edge cases, scalability, and overall behavior of the AI-driven PDF classification system as described. The implementation team may now build features based on these QA inputs.

**Test cases complete.**


            