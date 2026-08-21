import type { Member } from "../data/members";

interface MemberDetailsProps {
  member: Member;
}

export function MemberDetails({
  member,
}: MemberDetailsProps) {
  return (
    <div>
      <h1>Member Details</h1>

      <p>Member ID: {member.id}</p>

      <p>Name: {member.name}</p>

      <p>Status: {member.status}</p>

      <p>Email: {member.email}</p>

      <p>
        Savings Balance: $
        {member.savingsBalance.toLocaleString("en-US", {
          minimumFractionDigits: 2,
          maximumFractionDigits: 2,
        })}
      </p>
    </div>
  );
}