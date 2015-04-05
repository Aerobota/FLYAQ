package it.univaq.flyaq.rest;

import it.univaq.flyaq.rest.util.Util;

import java.io.InputStream;

import org.eclipse.core.runtime.FileLocator;
import org.eclipse.core.runtime.IConfigurationElement;
import org.eclipse.core.runtime.IExtension;
import org.eclipse.core.runtime.IExtensionPoint;
import org.eclipse.core.runtime.IRegistryEventListener;
import org.eclipse.core.runtime.Path;
import org.eclipse.core.runtime.Platform;
import org.osgi.framework.Bundle;

public class MissionPluginEventListener implements IRegistryEventListener {

	public MissionPluginEventListener() {
	}

	@Override
	public void added(IExtension[] extensions) {
		for (IExtension extension : extensions) {
			String exPoint = extension.getExtensionPointUniqueIdentifier();
			if (exPoint.equals("it.univaq.flyaq.extension.mission")) {
				IConfigurationElement[] confEls = extension
						.getConfigurationElements();
				for (IConfigurationElement confEl : confEls) {
					if (confEl.getName().equals("missionExtension")) {
						for (IConfigurationElement conf : confEl.getChildren()) {
							if (conf.getName().equals("Task")) {
								String iconPath = conf.getAttribute("icon");
								Bundle bundle = Platform.getBundle(extension
										.getContributor().getName());
								try {
									Path filePath = new Path(iconPath);
									InputStream stream = FileLocator
											.openStream(bundle, filePath, false);
									Util.copyFile(stream, filePath.lastSegment());
								} catch (Exception e) {
									e.printStackTrace();
								}
							}
						}
					}
				}
			}
		}
	}


	@Override
	public void removed(IExtension[] extensions) {
	}
	
	@Override
	public void added(IExtensionPoint[] arg0) {
	}

	@Override
	public void removed(IExtensionPoint[] arg0) {
	}

}
