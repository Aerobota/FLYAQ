/**
 *
 * $Id$
 */
package it.univaq.flyaq.mission.validation;

import it.univaq.flyaq.mission.Swarm;
import it.univaq.flyaq.mission.Task;
import it.univaq.flyaq.mission.TaskDependency;

import org.eclipse.emf.common.util.EList;

/**
 * A sample validator interface for {@link it.univaq.flyaq.mission.Mission}.
 * This doesn't really do anything, and it's not a real EMF artifact.
 * It was generated by the org.eclipse.emf.examples.generator.validator plug-in to illustrate how EMF's code generator can be extended.
 * This can be disabled with -vmargs -Dorg.eclipse.emf.examples.generator.validator=false.
 */
public interface MissionValidator {
	boolean validate();

	boolean validateCrs(String value);
	boolean validateTasks(EList<Task> value);
	boolean validateTaskDependencies(EList<TaskDependency> value);
	boolean validateSwarm(Swarm value);
}
