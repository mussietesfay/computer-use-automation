interface DashboardProps {
  onMemberSearch: () => void;
  onLogout: () => void;
}

export function Dashboard({
  onMemberSearch,
  onLogout,
}: DashboardProps) {
  return (
    <div>
      <h1>Bank Portal</h1>

      <button onClick={onLogout}>
        Logout
      </button>

      <h2>Dashboard</h2>

      <button onClick={onMemberSearch}>
        Member Search
      </button>
    </div>
  );
}