/**
 *
 * $Id$
 */
package it.univaq.flyaq.drone.validation;

import it.univaq.flyaq.drone.Action;
import it.univaq.flyaq.drone.Property;

import org.eclipse.emf.common.util.EList;

/**
 * A sample validator interface for {@link it.univaq.flyaq.drone.Device}.
 * This doesn't really do anything, and it's not a real EMF artifact.
 * It was generated by the org.eclipse.emf.examples.generator.validator plug-in to illustrate how EMF's code generator can be extended.
 * This can be disabled with -vmargs -Dorg.eclipse.emf.examples.generator.validator=false.
 */
public interface DeviceValidator {
	boolean validate();

	boolean validateSupportedActions(EList<Action> value);
	boolean validateProperties(EList<Property> value);
}
