
            ⏱ Total runtime: 1.26 minutes
            ---
            # 📋 Scrum AI Team Deliverables

## None
Build an AI driven app to extract the text from PDF and store into database. PDF have a fixed template with tables and sections to extract the information from.

## None
Transferred to ProductOwner

## ProductOwner
### Analysis of Business Objectives and Constraints:  
**Business Goals:**  
- Develop an AI-powered application to extract data from PDFs with a fixed template.  
- Organize extracted data into a structured database for further use.  

**Constraints:**  
- Ensure accurate extraction of text fields, tables, and sections.  
- Ensure compatibility with the fixed template format.  
- Must store data in a format suitable for querying within the database.  

## Epics for Backlog:  

### Epic 1:  
**Epic ID:** E1  
**Epic Title:** Design AI Model for Extracting Text and Structures from PDFs  
**Business Objective:** Accurately extract textual data, tables, and predefined sections from fixed-template PDFs using an AI-driven solution.  
**Business Value Score (1–10):** 9  
**Effort Estimate:** High  
**Priority Rank:** 1  

**Reasoning:** This epic is critical because the AI model is the foundation of the app's functionality. Although the effort is high, the business value of enabling text and table extraction is significant, placing it as the top priority.

---

### Epic 2:  
**Epic ID:** E2  
**Epic Title:** Develop Database Schema for Storing Extracted Data  
**Business Objective:** Create a database structure that supports organized storage, easy querying, and retrieval of extracted information.  
**Business Value Score (1–10):** 8  
**Effort Estimate:** Medium  
**Priority Rank:** 2  

**Reasoning:** The database design is essential for ensuring the extracted data can be stored and used efficiently. Its effort is moderate, and since it's a dependency for smooth integration, it ranks second after the AI extraction model.

---

### Epic 3:  
**Epic ID:** E3  
**Epic Title:** Build PDF File Upload and Preprocessing Module  
**Business Objective:** Allow users to upload PDFs and preprocess files to ensure compatibility with the AI model.  
**Business Value Score (1–10):** 7  
**Effort Estimate:** Medium  
**Priority Rank:** 3  

**Reasoning:** The preprocessing step is necessary to prepare PDFs for the extraction model. While important for user experience, its value is slightly lower compared to core extraction and data storage.  

---

### Epic 4:  
**Epic ID:** E4  
**Epic Title:** Create User Interface for PDF Upload and Retrieval of Extracted Data  
**Business Objective:** Provide an intuitive user interface for uploading PDFs and viewing extracted data.  
**Business Value Score (1–10):** 6  
**Effort Estimate:** Medium  
**Priority Rank:** 4  

**Reasoning:** A user-friendly interface is important for user adoption, but it adds less core product value compared to the back-end functionality.  

---

### Epic 5:  
**Epic ID:** E5  
**Epic Title:** Implement Error Handling and Data Validation Mechanisms  
**Business Objective:** Ensure robust data validation and error handling for accurate and reliable output.  
**Business Value Score (1–10):** 6  
**Effort Estimate:** Low  
**Priority Rank:** 5  

**Reasoning:** Error handling and validation improve accuracy and reliability but offer less direct value than the initial extraction and storage capabilities. Its low effort places it lower on the list.

---

### Epic 6:  
**Epic ID:** E6  
**Epic Title:** Optimize AI Model for Performance and Scalability  
**Business Objective:** Enhance AI model efficiency to handle large volumes of PDFs seamlessly.  
**Business Value Score (1–10):** 5  
**Effort Estimate:** High  
**Priority Rank:** 6  

**Reasoning:** Optimizing performance and scalability is essential in the long term but not as critical during the initial development phase. Its higher effort compared to immediate value places it at a lower priority.

---

### Epic Prioritization Explanation:  
The prioritization was determined using a value-to-effort ratio. High-value functions, such as text extraction and database design (E1 and E2), are ranked highest because they directly address core business goals. Lower-effort but moderately valued tasks (like E5) were postponed to allow focus on fully implementing essential mechanisms that deliver immediate business value.  

All Epics are clearly stated and aligned with product goals, ready to be converted into GitHub Epics.

## None
Transferred to BusinessAnalyst

## BusinessAnalyst
Here are **Agile user stories** based on your original input. Let’s break this requirement into smaller, testable stories to create a backlog:

---

### **Story 1: Extract Text from PDF Using AI Model**  
**As a** user,  
**I want to** extract textual content from a PDF with a fixed structure,  
**So that** the relevant text fields are retrieved for storage in the database.  

#### Assumptions:  
- PDF structure always follows the given fixed template.  
- No handwritten or ambiguous text is present in the PDF.

#### Functional Requirements:  
- The AI should detect and extract predefined text fields.  
- Successfully parse and extract text sections (e.g., headers, body, and static labels).  

#### Non-Functional Requirements:  
- The process should take no more than 5 seconds for a single PDF.  

#### Acceptance Criteria:  
- **Given** a PDF with the fixed structure,  
  **When** I pass it through the AI model,  
  **Then** the predefined text fields from the PDF structure should be correctly extracted into a structured format (e.g., JSON).  

---

### **Story 2: Extract Tables from PDF**  
**As a** user,  
**I want to** extract tabular data from a PDF,  
**So that** I can store the structured table rows and columns in the database.  

#### Assumptions:  
- Tables have a uniform format and consistent column naming.  
- Empty or partially filled cells can be handled.  

#### Functional Requirements:  
- Extract all rows and columns in a table.  
- Preserve the hierarchical structure if tables are nested.  

#### Edge Cases:  
- Empty cells should be returned as `null`.  
- Combined cells (spanning multiple columns/rows) should be split logically.  

#### Acceptance Criteria:  
- **Given** a PDF with a predefined table inside a fixed structure,  
  **When** the PDF is processed by the AI,  
  **Then** the tabular data should be extracted, split into rows and columns, and returned in a preconfigured data structure (e.g., JSON or CSV).  

---

### **Story 3: Save Processed Data into Database**  
**As a** system,  
**I want to** save the extracted text, table data, and section fields into the database,  
**So that** users can query and retrieve the information later.  

#### Assumptions:  
- The data will conform to the database schema (no transformations needed).  
- Duplicate entries in the database will be avoided through unique identifiers.  

#### Functional Requirements:  
- Map the extracted data to matching fields in the database schema.  
- Only save valid, non-empty data.  

#### Non-Functional Requirements:  
- Support a throughput of at least 100 PDFs per hour.  
- Database queries should retrieve the stored data within 250ms for small datasets.  

#### Acceptance Criteria:  
- **Given** extracted data from the AI model,  
  **When** the system saves the data into the database,  
  **Then** the data should be correctly mapped to schema fields and stored without errors.    

---

### **Story 4: Create PDF Upload and Preprocessing Module**  
**As a** user,  
**I want to** upload PDFs and validate their structure,  
**So that** I can ensure only valid PDFs are processed.  

#### Assumptions:  
- Invalid PDFs (e.g., missing sections) should trigger warnings and not be processed.  

#### Functional Requirements:  
- Provide an interface for uploading PDFs.  
- Perform a prevalidation check on the PDF structure.  
- Reject uploads for invalid formats.  

#### Non-Functional Requirements:  
- Each file upload and validation should complete within 10 seconds.  

#### Acceptance Criteria:  
- **Given** a PDF is uploaded through the module,  
  **When** the system validates its fixed structure,  
  **Then** the valid PDF should be accepted for further processing, and invalid files should trigger an error message/user notification.  

---

### **Story 5: Display Extracted Data to User via UI**  
**As a** user,  
**I want to** view the extracted text, tables, and section details in an organized layout,  
**So that** I can verify the results and ensure data integrity.  

#### Assumptions:  
- Extracted data will already be available in the backend database for retrieval.  

#### Functional Requirements:  
- Build a web UI with a preview feature to display stored data.  
- Highlight errors or missing data in the UI.  

#### Non-Functional Requirements:  
- The display should load in under 3 seconds.  
- Pagination support for long tabular data.  

#### Acceptance Criteria:  
- **Given** extracted data is stored in the database,  
  **When** I retrieve and view the data via the interface,  
  **Then** all the extracted text sections and tables should be presented accurately, without data gaps.    

---

### **Story 6: Handle Missing or Mismatched Data in Extraction**  
**As a** user,  
**I want to** receive notifications for missing sections or mismatched data in the PDF,  
**So that** I can fix issues before processing.  

#### Assumptions:  
- The validation logic for "mandatory fields" is known.  

#### Functional Requirements:  
- Log errors for missing sections or invalid content.  
- Notify the user of the issue through a user-friendly error message.  

#### Acceptance Criteria:  
- **Given** a PDF with missing or mismatched fields,  
  **When** the AI model processes the file,  
  **Then** the system should log errors and alert the user of any issues encountered.  

---

### Notes:  
These stories cover the core functionality of the application. Additional stories (like authentication, role-based access, or API integrations) can be written later if needed.  

**Are you happy with this breakdown, or should I add any edge cases you might have in mind?**

## None
Transferred to SolutionArchitect

## SolutionArchitect
Here is the **high-level solution architecture** for an AI-powered app designed to extract text from PDFs with fixed templates, process it, and store it in a database.

---

## **1. Major Components**

### **Frontend**
- **PDF Upload Interface**: A user interface (web or mobile) to upload PDF files.
- **Data Display UI**: A dashboard to display extracted text, tables, and section data in a user-friendly format.
- **Error Notification UI**: To inform users of processing issues, such as invalid formats or missing data.

### **Backend**
- **PDF Preprocessing Module**: 
  - Validates whether the input PDF conforms to the fixed template.
  - Handles file parsing (e.g., image-based PDF conversion via OCR if needed).
- **AI/ML Model for Data Extraction**:
  - Custom-trained Optical Character Recognition (OCR) powered by a tool like Tesseract, AWS Textract, or Google Vision AI.
  - Extracts structured data from text fields, tables, and sections in PDFs.
- **Data Transformation Module**:
  - Maps the extracted data into predefined data structures (e.g., JSON objects).
  - Performs data sanitization (e.g., parsing, formatting, resolving missing fields).
- **Data Storage Layer**:
  - Stores extracted data into a structured database (e.g., relational database like PostgreSQL or cloud-based options like AWS RDS/Google Cloud Spanner).
  - Support for storing raw PDF files and processed data for future reference.

### **Persistent Storage**
- **Database**:
  - Relational database (SQL): Tables to store text fields, hierarchical tables, and metadata.
- **File Storage**:
  - Cloud-based storage (e.g., AWS S3, Google Cloud Storage, Azure Blob Storage) for uploaded PDFs and logs.
- **Logs**:
  - Stores logs for debugging, such as missing data, exceptions, or runtime errors.
  
### **Authentication/Authorization Module**
- Role-based access control (RBAC) with frameworks like OAuth2.0 to secure data and limit access to authorized users only.

---

## **2. System Interactions**

### **Core Flow**
1. **PDF Upload**:  
   - User uploads a PDF via the UI.  
   - The file is sent to the backend for processing.

2. **Preprocessing and Validation**:  
   - PDF structure is validated to ensure that it meets the fixed template requirements.  
   - If valid, the file is passed to the data extraction module.  
   - If invalid, the user is notified via the UI.  

3. **Data Extraction**:  
   - The AI/ML model processes the PDF to extract textual sections and tables.  
   - The extracted data is structured (e.g., in JSON format).  

4. **Data Transformation and Mapping**:  
   - Extracted information is transformed/cleaned (e.g., handling null values).  
   - The system maps data to the predefined database schema.  

5. **Data Storage**:  
   - Cleaned and validated data is stored in a SQL database.  
   - The original PDF might also be saved in cloud-based object storage for future processing.  

6. **Frontend Query**:  
   - Users retrieve stored data via the interface.  
   - Data can be displayed in sections or tables for easy review.  

7. **Error Handling**:  
   - If OCR errors, missing fields, or processing issues occur, they are logged and surfaced to the user with actionable feedback.

---

## **3. Infrastructure Needs**

### **Cloud Provider**
- **AWS (recommended)**:
  - AWS Textract for text and table extraction.
  - AWS S3 for PDF storage.
  - AWS Lambda for serverless function execution during PDF upload and preprocessing.
  - AWS RDS for SQL-based database management.

- **Alternative Cloud Providers**:
  - Google Cloud (Google Vision AI, Google Cloud Storage, Firestore, BigQuery).
  - Microsoft Azure (Cognitive Services, Blob Storage, Azure SQL).

### **AI/ML Toolkit**
- **Tesseract OCR** (open-source) for text extraction from PDFs.
- **AWS Textract** or **Google Vision AI** for highly accurate OCR that recognizes tables and forms.

### **Frontend Tools**
- React or Angular for building a responsive, user-friendly web interface.
- Integration with REST APIs for seamless backend communication.

### **Backend Tech Stack**
- **Language**: Python (suitable for ML integration and handling libraries like PyPDF2, PDFplumber, or Pandas).
- **Framework**: Django or Flask for rapid API development.
- **Database**: PostgreSQL preferred for handling structured data storage with JSON compatibility.

### **Monitoring & Logging**
- CloudWatch (AWS) or ELK Stack (Elasticsearch, Logstash, Kibana) for logging and error monitoring.

---

## **4. Technical Dependencies**

1. **AI Model Accuracy**:
   - The OCR engine (Tesseract/AWS Textract) depending on the fixed template structure.
   - Edge cases like complex tables, multi-page PDFs, or uncommon font styles.

2. **Database Schema**:
   - Accurate schema design to properly map the extracted sections, tables, and text.

3. **Scalability Considerations**:
   - Handling increasing volumes of PDF uploads (e.g., via containerized backends—Docker/Kubernetes).
   - Support for batch uploads for enterprise use cases.

4. **Template Changes**:
   - The AI model and preprocessing module must adapt if the PDF template evolves over time.

---

## **5. Risks and Mitigation**

### **Risk 1: OCR Accuracy**
- **Description**: OCR might extract incorrect or incomplete data.  
- **Mitigation**: Use pretrained models (AWS Textract/Google Vision AI) and test rigorously with sample PDFs.

### **Risk 2: Handling Invalid PDFs**  
- **Description**: PDFs might deviate slightly from the fixed template.  
- **Mitigation**: Build strong prevalidation logic to detect and flag structural deviations.

### **Risk 3: Performance Bottlenecks**  
- **Description**: Processing large or complex PDFs could lead to slow workflows.  
- **Mitigation**: Implement parallel processing via serverless functions or worker queues (e.g., Celery, AWS Lambda).

### **Risk 4: Data Security**  
- **Description**: Sensitive data extracted from PDFs might require additional protection.  
- **Mitigation**: Encrypt data at rest and in transit (SSL, AES encryption, etc.). Implement strict access controls via IAM Policies or RBAC.

### **Risk 5: Storage Costs**  
- **Description**: Large PDFs or extracted data storage might increase operational costs over time.  
- **Mitigation**: Enforce retention policies for old PDFs or extracted data.

---

## **6. Additional Technical Stories**

1. **Story: Handle Multi-page PDFs**  
   - Extract and process data across multiple pages seamlessly.

2. **Story: Design Batch Processing**  
   - Allow users to upload multiple PDFs simultaneously for processing.

3. **Story: Enhance AI Accuracy with Fine-tuning**  
   - Train the OCR model specifically for the fixed template if off-the-shelf solutions don't meet accuracy thresholds.

4. **Story: Role-based User Access Management**  
   - Add authentication and authorization layers to secure uploads and data access.

---

This solution architecture covers all major components and provides a flexible, modular framework to build the AI-powered PDF processing app. Let me know if you'd like to adjust any details or dive deeper into specific parts!

## None
Transferred to QATester

## QATester
### Test Scenarios & Test Cases in Gherkin Syntax  
Below are the test scenarios and test cases for the AI-driven PDF text extraction app derived from the user stories and acceptance criteria. These test cases cover both the positive and edge cases:

---

### **Feature 1: Text Extraction from Fixed Template PDFs**

#### Test Scenario 1: Extract text sections successfully
```gherkin
Scenario: Extract textual content from a valid fixed-template PDF
Given a valid PDF file with a fixed structure is uploaded
When the AI model processes the file
Then the predefined text fields should be extracted correctly
And the extracted data should match the expected format
```

#### Test Scenario 2: Handle invalid PDF file structure
```gherkin
Scenario: Upload an invalid PDF file with mismatched structure
Given a PDF file that does not match the fixed template
When the file is uploaded for processing
Then the system should reject the file
And it should display an error message saying "Invalid PDF structure"
```

#### Test Scenario 3: Extract text from an empty template with no dynamic content
```gherkin
Scenario: Process a template with no data filled in required fields
Given a valid PDF template with empty mandatory fields is uploaded
When the AI model processes the file
Then a warning should be logged for missing fields
And the extracted data should return null for the missing fields
```

---

### **Feature 2: Table Extraction from PDFs**

#### Test Scenario 4: Extract tabular data successfully
```gherkin
Scenario: Extract tabular data from a valid PDF with a fixed table structure
Given a valid PDF file with a standard table is uploaded
When the AI model processes the file
Then the table data should be extracted row by row
And it should map each column to the correct data type in the schema
```

#### Test Scenario 5: Handle a table with merged cells
```gherkin
Scenario: Parse table data where some cells are merged
Given a valid PDF file where cells in the table are merged
When the AI model processes the file
Then the system should split the merged cells logically
And each value should be assigned to its corresponding row or column
```

---

### **Feature 3: Save Extracted Data into Database**

#### Test Scenario 6: Save extracted text fields and tables
```gherkin
Scenario: Save all extracted content into the database
Given a valid structured JSON is generated after extraction
When the system saves the content into the database
Then all text fields from the JSON should map correctly to the database schema
And no duplicate records should be inserted for the same PDF
```

#### Test Scenario 7: Handle database save failure due to schema mismatch
```gherkin
Scenario: Fail to save extracted data when schema mismatch occurs
Given the extracted data contains an unexpected field
When the system attempts to save the data to the database
Then the system should log an error stating "Schema validation error"
And the save operation should be aborted with no partial writes
```

---

### **Feature 4: PDF Upload Validation**

#### Test Scenario 8: Validate the structural integrity of PDFs during upload
```gherkin
Scenario: Upload a valid PDF that follows the pre-defined template
Given a PDF file is uploaded through the user interface
When the system validates the structural integrity of the PDF
Then the file should be accepted for processing
And no warnings should be displayed to the user
```

#### Test Scenario 9: Reject a corrupted PDF file
```gherkin
Scenario: Upload a corrupted or incomplete PDF file
Given a corrupted PDF file is uploaded through the system
When the system attempts to validate the file
Then an error message saying "Corrupted PDF" should be displayed
And the file should not be processed
```

---

### **Feature 5: Display Extracted Data in User Interface**

#### Test Scenario 10: Display extracted text and tables accurately
```gherkin
Scenario: Display extracted content in the user interface
Given the extracted data is stored in the backend database
When the user retrieves the content via the UI
Then the page should display all text sections and tables in an organized layout
And pagination should be available for tables with more than 20 rows
```

#### Test Scenario 11: Handle missing data in the UI
```gherkin
Scenario: Display a warning for missing fields in the extracted data
Given the extracted data is retrieved for a PDF containing missing fields
When the user views the results in the UI
Then the missing fields should be highlighted
And a warning message should inform the user about incomplete data
```

---

### **Feature 6: Error Handling and Notifications**

#### Test Scenario 12: Notify user of errors during data extraction
```gherkin
Scenario: Handle missing mandatory sections during extraction
Given a PDF is uploaded where mandatory sections are missing
When the AI model processes the file
Then the system should log an error for each missing section
And it should notify the user via the UI
And the extraction process should complete without crashing
```

#### Test Scenario 13: Retry mechanism on extraction failure
```gherkin
Scenario: Retry extracting data after an unexpected failure
Given a valid PDF is uploaded but processing fails due to a system error
When the system detects the error
Then it should retry the extraction process up to 3 times
And log the error if all retries fail
```

---

### **Feature 7: Security and Access Control**

#### Test Scenario 14: Restrict unauthorized access to sensitive data
```gherkin
Scenario: Prevent unauthorized users from accessing extraction results
Given a user is not logged in or has insufficient permissions
When they attempt to access stored data via the dashboard
Then access should be denied with a "403 Unauthorized" error
```

#### Test Scenario 15: Encrypt sensitive extracted data
```gherkin
Scenario: Store extracted PDF data securely in the database
Given the system processes confidential data from the PDF
When the data is stored in the database
Then it should be encrypted using AES-256 encryption
And only authorized users can decrypt and view the data
```

---

### **Feature 8: Performance and Scalability**

#### Test Scenario 16: Bulk process multiple PDFs concurrently
```gherkin
Scenario: Handle batch uploads of multiple PDFs
Given 50 valid PDFs are uploaded simultaneously
When the system begins processing the files
Then each file should be processed without delays
And the system should complete all extractions within 10 minutes
```

#### Test Scenario 17: Measure time performance for a single PDF
```gherkin
Scenario: Ensure a single PDF is processed within the expected time frame
Given a single 2-page PDF is uploaded
When the AI model processes the file
Then the entire extraction process should complete in under 5 seconds
```

---

### **Conclusion**
The above test scripts ensure that all scenarios—functional, edge cases, error handling, and performance benchmarks—are covered for the AI-driven PDF processing application.

**Test cases complete.**


            