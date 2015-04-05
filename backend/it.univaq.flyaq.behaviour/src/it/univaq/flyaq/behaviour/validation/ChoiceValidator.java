/**
 *
 * $Id$
 */
package it.univaq.flyaq.behaviour.validation;

import it.univaq.flyaq.behaviour.Move;

/**
 * A sample validator interface for {@link it.univaq.flyaq.behaviour.Choice}.
 * This doesn't really do anything, and it's not a real EMF artifact.
 * It was generated by the org.eclipse.emf.examples.generator.validator plug-in to illustrate how EMF's code generator can be extended.
 * This can be disabled with -vmargs -Dorg.eclipse.emf.examples.generator.validator=false.
 */
public interface ChoiceValidator {
	boolean validate();

	boolean validateConditionIdentifier(String value);
	boolean validateFalseBranch(Move value);
}
