import { useState } from "react";

import { Login } from "./components/Login";
import { Dashboard } from "./components/Dashboard";
import { MemberSearch } from "./components/MemberSearch";
import { MemberDetails } from "./components/MemberDetails";

import { members, type Member } from "./data/members";

type Page =
  | "login"
  | "dashboard"
  | "member-search"
  | "member-details";

function App() {
  const [page, setPage] = useState<Page>("login");
  const [selectedMember, setSelectedMember] =
    useState<Member | null>(null);

  function handleLogin() {
    setPage("dashboard");
  }

  function handleLogout() {
    setSelectedMember(null);
    setPage("login");
  }

  function handleMemberSearch(memberId: string) {
    const member = members.find(
      (item) => item.id === memberId
    );

    if (!member) {
      alert("Member not found");
      return;
    }

    setSelectedMember(member);
    setPage("member-details");
  }

  if (page === "login") {
    return <Login onLogin={handleLogin} />;
  }

  if (page === "dashboard") {
    return (
      <Dashboard
        onMemberSearch={() =>
          setPage("member-search")
        }
        onLogout={handleLogout}
      />
    );
  }

  if (page === "member-search") {
    return (
      <MemberSearch
        onSearch={handleMemberSearch}
      />
    );
  }

  if (page === "member-details" && selectedMember) {
    return (
      <MemberDetails
        member={selectedMember}
      />
    );
  }

  return null;
}

export default App;