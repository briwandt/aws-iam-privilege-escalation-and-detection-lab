# Remediation Policy

To prevent the privilege escalation path explored in this lab, the developer's IAM policy must be restricted. The original policy allowed the developer to create any Lambda function and pass any IAM role to it, enabling them to assume the privileges of the highly permissive iam-escalation-lab-lambda-role.

The remediated policy restricts the developer to:
- Creating, updating, and invoking Lambda functions whose names start with iam-escalation-lab-approved-
- Passing only the approved role iam-escalation-lab-approved-role

## Files

- [safer-developer-policy.json](safer-developer-policy.json): The remediated, secure IAM policy for the developer.

## Verification

When the developer attempts to create a Lambda function (iam-escalation-lab-remediation-test) using the sensitive role (iam-escalation-lab-lambda-role), the request is blocked by IAM with an AccessDeniedException.

Evidence of the blocked attempt is shown in [screenshots/12-remediation-create-function-denied.png](../screenshots/12-remediation-create-function-denied.png).
