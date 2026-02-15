# Requirements Document

## Introduction

BharatAI Saathi is an AI-powered platform designed to bridge the gap between Indian citizens and government welfare schemes. The system addresses the critical problem of millions of citizens missing out on government benefits due to lack of awareness, complex eligibility criteria, and language barriers. The platform provides personalized scheme recommendations, eligibility scoring, document verification, application guidance, and an accessible chat interface with voice support for low-literacy users.

## Glossary

- **Citizen**: An Indian citizen who uses the platform to discover and apply for government schemes
- **Scheme**: A government welfare program (Central, State, or Local) with specific eligibility criteria and benefits
- **User_Profile**: A data structure containing citizen attributes (age, gender, income, state, category)
- **Eligibility_Score**: A percentage value (0-100) indicating how well a citizen matches a scheme's criteria
- **Recommendation_Engine**: The system component that matches citizens with eligible schemes
- **Chat_Assistant**: The conversational AI interface that guides citizens through the platform
- **Document_Verifier**: The AI component that validates uploaded documents against scheme requirements
- **Notification_Service**: The system component that alerts citizens about new eligible schemes
- **Application_Tracker**: The system component that monitors the status of scheme applications

## Requirements

### Requirement 1: User Profile Management

**User Story:** As a citizen, I want to create and manage my profile with personal details, so that the system can recommend schemes relevant to my situation.

#### Acceptance Criteria

1. WHEN a citizen provides profile information (age, gender, income, state, category), THE User_Profile_Manager SHALL validate and store the data
2. WHEN a citizen updates their profile, THE User_Profile_Manager SHALL recalculate scheme recommendations based on the new information
3. THE User_Profile_Manager SHALL ensure age is a positive integer between 0 and 120
4. THE User_Profile_Manager SHALL ensure income is a non-negative integer
5. THE User_Profile_Manager SHALL validate state against a list of valid Indian states and union territories
6. THE User_Profile_Manager SHALL validate category against predefined categories (General, OBC, SC, ST, EWS)
7. WHEN profile data is stored, THE User_Profile_Manager SHALL encrypt sensitive information

### Requirement 2: Scheme Recommendation

**User Story:** As a citizen, I want to receive personalized scheme recommendations based on my profile, so that I can discover benefits I'm eligible for.

#### Acceptance Criteria

1. WHEN a citizen requests recommendations, THE Recommendation_Engine SHALL return schemes sorted by eligibility score in descending order
2. WHEN calculating eligibility, THE Recommendation_Engine SHALL assign scores based on age match (20 points), gender match (15 points), income eligibility (25 points), state match (20 points), and category match (20 points)
3. THE Recommendation_Engine SHALL only recommend schemes with eligibility scores above 40%
4. WHEN multiple schemes have the same score, THE Recommendation_Engine SHALL maintain consistent ordering
5. WHEN a scheme has no age restrictions, THE Recommendation_Engine SHALL treat all ages as eligible for that criterion
6. WHEN a scheme is marked as "all states", THE Recommendation_Engine SHALL match citizens from any state
7. WHEN a scheme is marked as "any gender", THE Recommendation_Engine SHALL match citizens of all genders

### Requirement 3: Eligibility Score Calculation

**User Story:** As a citizen, I want to see a clear eligibility percentage for each scheme, so that I understand my chances of qualifying.

#### Acceptance Criteria

1. THE Eligibility_Calculator SHALL compute scores as a percentage from 0 to 100
2. WHEN displaying scores, THE Eligibility_Calculator SHALL round to the nearest integer
3. FOR ALL schemes, THE Eligibility_Calculator SHALL apply the same scoring formula consistently
4. WHEN a citizen meets all criteria, THE Eligibility_Calculator SHALL return a score of 100
5. WHEN a citizen meets no criteria, THE Eligibility_Calculator SHALL return a score of 0

### Requirement 4: Scheme Information Display

**User Story:** As a citizen, I want to view detailed information about recommended schemes, so that I can understand the benefits and requirements.

#### Acceptance Criteria

1. WHEN displaying a scheme, THE Scheme_Display SHALL show the scheme name, description, eligibility criteria, benefits, and required documents
2. THE Scheme_Display SHALL present information in simple, clear language appropriate for citizens with varying literacy levels
3. WHEN a scheme has complex eligibility rules, THE Scheme_Display SHALL break them down into easy-to-understand points
4. THE Scheme_Display SHALL highlight which eligibility criteria the citizen meets and which they don't
5. WHEN a scheme requires specific documents, THE Scheme_Display SHALL list each document with a brief explanation

### Requirement 5: Document Verification

**User Story:** As a citizen, I want to upload and verify my documents against scheme requirements, so that I can ensure I have the correct paperwork before applying.

#### Acceptance Criteria

1. WHEN a citizen uploads a document, THE Document_Verifier SHALL validate the file format (PDF, JPG, PNG)
2. WHEN a document is uploaded, THE Document_Verifier SHALL check file size does not exceed 10MB
3. WHEN verifying documents, THE Document_Verifier SHALL extract text and validate against scheme requirements
4. IF a document is missing required information, THEN THE Document_Verifier SHALL provide specific feedback on what is missing
5. WHEN all required documents are verified, THE Document_Verifier SHALL mark the citizen as ready to apply
6. THE Document_Verifier SHALL store document verification status for each scheme application
7. WHEN a document verification fails, THE Document_Verifier SHALL provide clear guidance on how to correct the issue

### Requirement 6: Application Guidance

**User Story:** As a citizen, I want step-by-step guidance through the application process, so that I can successfully apply for schemes without confusion.

#### Acceptance Criteria

1. WHEN a citizen starts an application, THE Application_Guide SHALL provide a sequential list of steps required to complete the application
2. THE Application_Guide SHALL track which steps have been completed and which remain
3. WHEN a step is completed, THE Application_Guide SHALL automatically advance to the next step
4. THE Application_Guide SHALL provide links to official government portals where applications must be submitted
5. WHEN a citizen needs help with a step, THE Application_Guide SHALL provide contextual assistance and examples
6. THE Application_Guide SHALL allow citizens to save progress and resume later

### Requirement 7: AI Chat Assistant

**User Story:** As a citizen, I want to interact with an AI assistant through a chat interface, so that I can get personalized help and answers to my questions.

#### Acceptance Criteria

1. WHEN a citizen sends a message, THE Chat_Assistant SHALL respond within 3 seconds
2. THE Chat_Assistant SHALL understand queries in English and Hindi
3. WHEN a citizen asks about schemes, THE Chat_Assistant SHALL provide relevant recommendations based on their profile
4. WHEN a citizen asks about eligibility, THE Chat_Assistant SHALL explain criteria in simple language
5. THE Chat_Assistant SHALL maintain conversation context across multiple messages
6. WHEN a citizen asks an unclear question, THE Chat_Assistant SHALL ask clarifying questions
7. THE Chat_Assistant SHALL provide a WhatsApp-style interface with message bubbles and timestamps

### Requirement 8: Voice Support

**User Story:** As a low-literacy citizen, I want to use voice input and output, so that I can access the platform without needing to read or type.

#### Acceptance Criteria

1. WHEN a citizen activates voice input, THE Voice_Interface SHALL convert speech to text with at least 85% accuracy
2. THE Voice_Interface SHALL support Hindi and English voice input
3. WHEN the system responds, THE Voice_Interface SHALL convert text responses to natural-sounding speech
4. THE Voice_Interface SHALL allow citizens to interrupt voice output
5. WHEN voice recognition fails, THE Voice_Interface SHALL ask the citizen to repeat their input
6. THE Voice_Interface SHALL provide visual feedback indicating when it is listening

### Requirement 9: Notification System

**User Story:** As a citizen, I want to receive notifications about new schemes I'm eligible for, so that I don't miss opportunities.

#### Acceptance Criteria

1. WHEN a new scheme is added to the system, THE Notification_Service SHALL identify all eligible citizens based on their profiles
2. THE Notification_Service SHALL send notifications to eligible citizens within 24 hours of scheme addition
3. WHEN a citizen's profile changes, THE Notification_Service SHALL check for newly eligible schemes
4. THE Notification_Service SHALL allow citizens to configure notification preferences (email, SMS, in-app)
5. THE Notification_Service SHALL not send duplicate notifications for the same scheme
6. WHEN a scheme deadline is approaching, THE Notification_Service SHALL send reminder notifications to citizens who haven't applied

### Requirement 10: Multi-Language Support

**User Story:** As a citizen who prefers my regional language, I want to use the platform in my preferred language, so that I can understand information clearly.

#### Acceptance Criteria

1. THE Language_Manager SHALL support English and Hindi as primary languages
2. WHEN a citizen selects a language, THE Language_Manager SHALL display all interface text in that language
3. THE Language_Manager SHALL translate scheme information while preserving accuracy
4. WHEN translating technical terms, THE Language_Manager SHALL provide both the translation and the original term
5. THE Language_Manager SHALL remember the citizen's language preference across sessions

### Requirement 11: Scheme Data Management

**User Story:** As a system administrator, I want to add and update scheme information, so that the platform always has current and accurate data.

#### Acceptance Criteria

1. WHEN an administrator adds a new scheme, THE Scheme_Manager SHALL validate all required fields are present
2. THE Scheme_Manager SHALL store schemes with attributes including name, description, age_min, age_max, gender, income_max, state, category, benefits, and required_documents
3. WHEN a scheme is updated, THE Scheme_Manager SHALL maintain a version history
4. THE Scheme_Manager SHALL support bulk import of schemes from CSV or JSON format
5. WHEN a scheme is marked as inactive, THE Scheme_Manager SHALL exclude it from recommendations but preserve historical data
6. THE Scheme_Manager SHALL validate that age_min is less than or equal to age_max
7. THE Scheme_Manager SHALL validate that income_max is a positive number

### Requirement 12: API Interface

**User Story:** As a frontend developer, I want a well-documented REST API, so that I can build user interfaces that interact with the backend.

#### Acceptance Criteria

1. THE API_Server SHALL provide endpoints for user profile management, scheme recommendations, document upload, and chat interactions
2. WHEN an API request is received, THE API_Server SHALL validate request format and return appropriate error messages for invalid requests
3. THE API_Server SHALL return responses in JSON format
4. THE API_Server SHALL include appropriate HTTP status codes (200 for success, 400 for bad request, 401 for unauthorized, 500 for server error)
5. THE API_Server SHALL implement rate limiting to prevent abuse (maximum 100 requests per minute per user)
6. THE API_Server SHALL require authentication for all endpoints except health check
7. WHEN an error occurs, THE API_Server SHALL return error messages that are helpful for debugging without exposing sensitive system information

### Requirement 13: Authentication and Security

**User Story:** As a citizen, I want my personal information to be secure, so that my privacy is protected.

#### Acceptance Criteria

1. WHEN a citizen creates an account, THE Auth_System SHALL require a strong password (minimum 8 characters, including uppercase, lowercase, and numbers)
2. THE Auth_System SHALL hash passwords using a secure algorithm before storage
3. WHEN a citizen logs in, THE Auth_System SHALL issue a JWT token valid for 24 hours
4. THE Auth_System SHALL implement session timeout after 30 minutes of inactivity
5. WHEN multiple failed login attempts occur (more than 5), THE Auth_System SHALL temporarily lock the account for 15 minutes
6. THE Auth_System SHALL support password reset via email or SMS verification
7. THE Auth_System SHALL log all authentication events for security auditing

### Requirement 14: Data Privacy and Compliance

**User Story:** As a citizen, I want my data to be handled according to privacy laws, so that my rights are protected.

#### Acceptance Criteria

1. THE Privacy_Manager SHALL allow citizens to view all data stored about them
2. THE Privacy_Manager SHALL allow citizens to request deletion of their data
3. WHEN a citizen requests data deletion, THE Privacy_Manager SHALL remove all personal information within 30 days
4. THE Privacy_Manager SHALL obtain explicit consent before collecting sensitive information
5. THE Privacy_Manager SHALL not share citizen data with third parties without explicit consent
6. THE Privacy_Manager SHALL maintain audit logs of all data access and modifications

### Requirement 15: Performance and Scalability

**User Story:** As a citizen, I want the platform to respond quickly even during high traffic, so that I can access information without delays.

#### Acceptance Criteria

1. WHEN a citizen requests scheme recommendations, THE System SHALL return results within 2 seconds for profiles with up to 1000 schemes
2. THE System SHALL support at least 1000 concurrent users without performance degradation
3. WHEN the scheme database grows, THE System SHALL maintain response times through efficient indexing
4. THE System SHALL cache frequently accessed scheme data to improve performance
5. WHEN system load exceeds 80% capacity, THE System SHALL scale resources automatically
