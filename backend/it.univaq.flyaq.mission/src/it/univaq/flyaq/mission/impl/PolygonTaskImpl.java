/**
 */
package it.univaq.flyaq.mission.impl;

import it.univaq.flyaq.mission.Coordinate;
import it.univaq.flyaq.mission.MissionPackage;
import it.univaq.flyaq.mission.PolygonTask;

import java.util.Collection;

import org.eclipse.emf.common.notify.Notification;
import org.eclipse.emf.common.notify.NotificationChain;

import org.eclipse.emf.common.util.EList;

import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.InternalEObject;

import org.eclipse.emf.ecore.impl.ENotificationImpl;

import org.eclipse.emf.ecore.util.EObjectContainmentEList;
import org.eclipse.emf.ecore.util.InternalEList;

/**
 * <!-- begin-user-doc -->
 * An implementation of the model object '<em><b>Polygon Task</b></em>'.
 * <!-- end-user-doc -->
 * <p>
 * The following features are implemented:
 * <ul>
 *   <li>{@link it.univaq.flyaq.mission.impl.PolygonTaskImpl#getShell <em>Shell</em>}</li>
 *   <li>{@link it.univaq.flyaq.mission.impl.PolygonTaskImpl#getInitialPosition <em>Initial Position</em>}</li>
 * </ul>
 * </p>
 *
 * @generated
 */
public abstract class PolygonTaskImpl extends TaskImpl implements PolygonTask {
	/**
	 * The cached value of the '{@link #getShell() <em>Shell</em>}' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getShell()
	 * @generated
	 * @ordered
	 */
	protected EList<Coordinate> shell;

	/**
	 * The cached value of the '{@link #getInitialPosition() <em>Initial Position</em>}' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getInitialPosition()
	 * @generated
	 * @ordered
	 */
	protected Coordinate initialPosition;

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected PolygonTaskImpl() {
		super();
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	protected EClass eStaticClass() {
		return MissionPackage.Literals.POLYGON_TASK;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public EList<Coordinate> getShell() {
		if (shell == null) {
			shell = new EObjectContainmentEList<Coordinate>(Coordinate.class, this, MissionPackage.POLYGON_TASK__SHELL);
		}
		return shell;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public Coordinate getInitialPosition() {
		return initialPosition;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public NotificationChain basicSetInitialPosition(Coordinate newInitialPosition, NotificationChain msgs) {
		Coordinate oldInitialPosition = initialPosition;
		initialPosition = newInitialPosition;
		if (eNotificationRequired()) {
			ENotificationImpl notification = new ENotificationImpl(this, Notification.SET, MissionPackage.POLYGON_TASK__INITIAL_POSITION, oldInitialPosition, newInitialPosition);
			if (msgs == null) msgs = notification; else msgs.add(notification);
		}
		return msgs;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public void setInitialPosition(Coordinate newInitialPosition) {
		if (newInitialPosition != initialPosition) {
			NotificationChain msgs = null;
			if (initialPosition != null)
				msgs = ((InternalEObject)initialPosition).eInverseRemove(this, EOPPOSITE_FEATURE_BASE - MissionPackage.POLYGON_TASK__INITIAL_POSITION, null, msgs);
			if (newInitialPosition != null)
				msgs = ((InternalEObject)newInitialPosition).eInverseAdd(this, EOPPOSITE_FEATURE_BASE - MissionPackage.POLYGON_TASK__INITIAL_POSITION, null, msgs);
			msgs = basicSetInitialPosition(newInitialPosition, msgs);
			if (msgs != null) msgs.dispatch();
		}
		else if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, MissionPackage.POLYGON_TASK__INITIAL_POSITION, newInitialPosition, newInitialPosition));
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public NotificationChain eInverseRemove(InternalEObject otherEnd, int featureID, NotificationChain msgs) {
		switch (featureID) {
			case MissionPackage.POLYGON_TASK__SHELL:
				return ((InternalEList<?>)getShell()).basicRemove(otherEnd, msgs);
			case MissionPackage.POLYGON_TASK__INITIAL_POSITION:
				return basicSetInitialPosition(null, msgs);
		}
		return super.eInverseRemove(otherEnd, featureID, msgs);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Object eGet(int featureID, boolean resolve, boolean coreType) {
		switch (featureID) {
			case MissionPackage.POLYGON_TASK__SHELL:
				return getShell();
			case MissionPackage.POLYGON_TASK__INITIAL_POSITION:
				return getInitialPosition();
		}
		return super.eGet(featureID, resolve, coreType);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@SuppressWarnings("unchecked")
	@Override
	public void eSet(int featureID, Object newValue) {
		switch (featureID) {
			case MissionPackage.POLYGON_TASK__SHELL:
				getShell().clear();
				getShell().addAll((Collection<? extends Coordinate>)newValue);
				return;
			case MissionPackage.POLYGON_TASK__INITIAL_POSITION:
				setInitialPosition((Coordinate)newValue);
				return;
		}
		super.eSet(featureID, newValue);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void eUnset(int featureID) {
		switch (featureID) {
			case MissionPackage.POLYGON_TASK__SHELL:
				getShell().clear();
				return;
			case MissionPackage.POLYGON_TASK__INITIAL_POSITION:
				setInitialPosition((Coordinate)null);
				return;
		}
		super.eUnset(featureID);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public boolean eIsSet(int featureID) {
		switch (featureID) {
			case MissionPackage.POLYGON_TASK__SHELL:
				return shell != null && !shell.isEmpty();
			case MissionPackage.POLYGON_TASK__INITIAL_POSITION:
				return initialPosition != null;
		}
		return super.eIsSet(featureID);
	}

} //PolygonTaskImpl
