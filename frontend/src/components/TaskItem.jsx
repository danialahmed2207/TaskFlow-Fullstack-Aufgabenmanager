/**
 * Einzelne Task-Komponente
 * Trennt die Darstellung einer Aufgabe vom Haupt-App-Container.
 */
export default function TaskItem({ task, onToggle, onDelete }) {
  return (
    <li className={task.completed ? 'completed' : ''}>
      <div className="task-content">
        <strong>{task.title}</strong>
        {task.description && <span>{task.description}</span>}
      </div>
      <div className="task-actions">
        <button
          className="toggle-btn"
          onClick={() => onToggle(task)}
          title={task.completed ? 'Rückgängig' : 'Erledigt'}
        >
          {task.completed ? '↩️' : '✅'}
        </button>
        <button
          className="delete-btn"
          onClick={() => onDelete(task.id)}
          title="Löschen"
        >
          🗑️
        </button>
      </div>
    </li>
  )
}
