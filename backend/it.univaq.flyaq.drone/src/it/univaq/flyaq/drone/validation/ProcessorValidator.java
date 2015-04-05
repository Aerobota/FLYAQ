/**
 *
 * $Id$
 */
package it.univaq.flyaq.drone.validation;


/**
 * A sample validator interface for {@link it.univaq.flyaq.drone.Processor}.
 * This doesn't really do anything, and it's not a real EMF artifact.
 * It was generated by the org.eclipse.emf.examples.generator.validator plug-in to illustrate how EMF's code generator can be extended.
 * This can be disabled with -vmargs -Dorg.eclipse.emf.examples.generator.validator=false.
 */
public interface ProcessorValidator {
	boolean validate();

	boolean validateArchitecture(String value);
	boolean validateFrequency(int value);
}
