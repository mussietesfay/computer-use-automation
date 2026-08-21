import { useState } from "react";

interface MemberSearchProps {
  onSearch: (memberId: string) => void;
}

export function MemberSearch({
  onSearch,
}: MemberSearchProps) {
  const [memberId, setMemberId] = useState("");

  function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();

    onSearch(memberId);
  }

  return (
    <div>
      <h1>Member Search</h1>

      <form onSubmit={handleSubmit}>
        <label htmlFor="member-id">
          Member ID
        </label>

        <input
          id="member-id"
          value={memberId}
          onChange={(event) => setMemberId(event.target.value)}
        />

        <button type="submit">
          Search
        </button>
      </form>
    </div>
  );
}