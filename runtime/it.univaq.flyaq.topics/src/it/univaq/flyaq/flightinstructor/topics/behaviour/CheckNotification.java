package it.univaq.flyaq.flightinstructor.topics.behaviour;

import javax.json.JsonArray;
import javax.json.JsonObject;

/**
 * A representation of the model object '<em><b>CheckNotification</b></em>'.
 * <!-- begin-user-doc --> <!-- end-user-doc -->
 * 
 * @generated
 */
public class CheckNotification extends CommunicationAction {

	/**
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	private Slot slot = null;
	
	public CheckNotification(JsonObject jsonObject, Behaviour behaviour) {
		super(jsonObject);
		this.slot = behaviour.getSlotByName(jsonObject.getString("slot_name"));
	}

	/**
	 * Returns the value of '<em><b>slot</b></em>' feature.
	 * 
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @return the value of '<em><b>slot</b></em>' feature
	 * @generated
	 */
	public Slot getSlot() {
		return slot;
	}

	/**
	 * Sets the '{@link CheckNotification#getSlot() <em>slot</em>}' feature.
	 * 
	 * <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @param newSlot
	 *            the new value of the '{@link CheckNotification#getSlot() slot}
	 *            ' feature.
	 * @generated
	 */
	public void setSlot(Slot newSlot) {
		slot = newSlot;
	}

	/**
	 * A toString method which prints the values of all EAttributes of this
	 * instance. <!-- begin-user-doc --> <!-- end-user-doc -->
	 * 
	 * @generated
	 */
	@Override
	public String toString() {
		return "CheckNotification ";
	}
}
