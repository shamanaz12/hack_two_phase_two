# Data Model: General Update Feature

**Feature**: 001-update-feature
**Date**: 2026-01-13

## Overview

This document defines the data models for the update feature of the Hackathon Todo Application. The models are based on the existing system requirements and the update functionality needed.

## Entity Definitions

### 1. Update Entity

**Entity Name**: Update
- **Fields**:
  - id: Integer (Primary Key, Auto-generated)
  - title: String (Required, Max length: 100)
  - description: Text (Optional)
  - status: String (Required, Enum: 'pending', 'in-progress', 'completed', 'failed')
  - version: String (Required, e.g., 'v1.0.0')
  - created_at: DateTime (Auto-generated)
  - updated_at: DateTime (Auto-generated)
  - applied_at: DateTime (Optional, when update was applied)
  - rollback_possible: Boolean (Default: True)

**Validation Rules**:
- Title must be 1-100 characters
- Status must be one of the allowed values
- Version must follow semantic versioning format
- Update cannot be applied if status is 'failed'

**Relationships**:
- One-to-many with UpdateLog (one update can have many log entries)

### 2. Update Log Entity

**Entity Name**: UpdateLog
- **Fields**:
  - id: Integer (Primary Key, Auto-generated)
  - update_id: Integer (Foreign Key to Update)
  - timestamp: DateTime (Auto-generated)
  - level: String (Required, Enum: 'info', 'warning', 'error', 'critical')
  - message: Text (Required)
  - component: String (Optional, which system component was affected)

**Validation Rules**:
- Level must be one of the allowed values
- Message cannot be empty
- Update ID must reference an existing Update record

**Relationships**:
- Many-to-one with Update (many logs can belong to one update)

### 3. Task Entity (Existing - Updated)

**Entity Name**: Task (as defined in project constitution)
- **Fields**:
  - id: Integer (Primary Key, Auto-generated)
  - title: String (Required, Max length: 200)
  - description: Text (Optional)
  - completed: Boolean (Default: False)
  - user_id: Integer (Foreign Key to User, managed by Better Auth)
  - created_at: DateTime (Auto-generated)
  - updated_at: DateTime (Auto-generated)

**Validation Rules**:
- Title must be 1-200 characters
- User ID must reference an existing user
- Cannot be deleted if referenced by other entities (if applicable)

**State Transitions**:
- Default state: completed = False
- State change: completed can transition from False to True or True to False via PATCH /api/{user_id}/tasks/{id}/complete

## Data Flow

### Update Process
1. An Update entity is created with status 'pending'
2. As the update progresses, UpdateLog entries are created with relevant information
3. When complete, the Update status changes to 'completed' and applied_at is set
4. If issues occur, status changes to 'failed' and appropriate logs are recorded

### Rollback Capability
- Updates marked with rollback_possible = True can be reversed
- Rollback process creates new UpdateLog entries documenting the rollback
- System state is restored to pre-update condition

## Constraints

### Referential Integrity
- All foreign key relationships must reference valid records
- Cascading deletes are disabled to prevent accidental data loss

### Data Validation
- All required fields must be present before saving
- Field length limits must be enforced
- Enum values must be validated before saving

### Audit Trail
- All update activities must be logged in UpdateLog
- Timestamps must be accurate and consistent
- Component information must be included when available