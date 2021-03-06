/**
 */
package it.univaq.flyaq.behaviour;

import org.eclipse.emf.ecore.EObject;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Coordinate</b></em>'.
 * <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * <ul>
 *   <li>{@link it.univaq.flyaq.behaviour.Coordinate#getLatitude <em>Latitude</em>}</li>
 *   <li>{@link it.univaq.flyaq.behaviour.Coordinate#getLongitude <em>Longitude</em>}</li>
 *   <li>{@link it.univaq.flyaq.behaviour.Coordinate#getAltitude <em>Altitude</em>}</li>
 *   <li>{@link it.univaq.flyaq.behaviour.Coordinate#getHeading <em>Heading</em>}</li>
 * </ul>
 * </p>
 *
 * @see it.univaq.flyaq.behaviour.BehaviourPackage#getCoordinate()
 * @model
 * @generated
 */
public interface Coordinate extends EObject {
	/**
	 * Returns the value of the '<em><b>Latitude</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Latitude</em>' attribute isn't clear,
	 * there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Latitude</em>' attribute.
	 * @see #setLatitude(float)
	 * @see it.univaq.flyaq.behaviour.BehaviourPackage#getCoordinate_Latitude()
	 * @model required="true"
	 * @generated
	 */
	float getLatitude();

	/**
	 * Sets the value of the '{@link it.univaq.flyaq.behaviour.Coordinate#getLatitude <em>Latitude</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Latitude</em>' attribute.
	 * @see #getLatitude()
	 * @generated
	 */
	void setLatitude(float value);

	/**
	 * Returns the value of the '<em><b>Longitude</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Longitude</em>' attribute isn't clear,
	 * there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Longitude</em>' attribute.
	 * @see #setLongitude(float)
	 * @see it.univaq.flyaq.behaviour.BehaviourPackage#getCoordinate_Longitude()
	 * @model required="true"
	 * @generated
	 */
	float getLongitude();

	/**
	 * Sets the value of the '{@link it.univaq.flyaq.behaviour.Coordinate#getLongitude <em>Longitude</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Longitude</em>' attribute.
	 * @see #getLongitude()
	 * @generated
	 */
	void setLongitude(float value);

	/**
	 * Returns the value of the '<em><b>Altitude</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Altitude</em>' attribute isn't clear,
	 * there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Altitude</em>' attribute.
	 * @see #setAltitude(float)
	 * @see it.univaq.flyaq.behaviour.BehaviourPackage#getCoordinate_Altitude()
	 * @model required="true"
	 * @generated
	 */
	float getAltitude();

	/**
	 * Sets the value of the '{@link it.univaq.flyaq.behaviour.Coordinate#getAltitude <em>Altitude</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Altitude</em>' attribute.
	 * @see #getAltitude()
	 * @generated
	 */
	void setAltitude(float value);

	/**
	 * Returns the value of the '<em><b>Heading</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>Heading</em>' attribute isn't clear,
	 * there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Heading</em>' attribute.
	 * @see #setHeading(float)
	 * @see it.univaq.flyaq.behaviour.BehaviourPackage#getCoordinate_Heading()
	 * @model
	 * @generated
	 */
	float getHeading();

	/**
	 * Sets the value of the '{@link it.univaq.flyaq.behaviour.Coordinate#getHeading <em>Heading</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Heading</em>' attribute.
	 * @see #getHeading()
	 * @generated
	 */
	void setHeading(float value);

} // Coordinate
