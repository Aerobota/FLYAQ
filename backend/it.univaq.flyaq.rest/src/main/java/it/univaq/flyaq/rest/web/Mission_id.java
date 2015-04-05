package it.univaq.flyaq.rest.web;

import java.net.URLDecoder;

import it.univaq.flyaq.mission.Mission;
import it.univaq.flyaq.rest.exception.SessionNotFoundException;
import it.univaq.flyaq.rest.jsonbridge.JsonBridge;
import it.univaq.flyaq.rest.session.Session;
import it.univaq.flyaq.rest.session.Sessions;

import javax.servlet.http.HttpServletResponse;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import com.fasterxml.jackson.core.JsonParseException;

@Controller
public final class Mission_id {

	@RequestMapping(value = "/v1/mission/{ID}", method = RequestMethod.POST)
	public void postMission(@PathVariable("ID") String ID, @RequestBody String payload, HttpServletResponse httpServletResponse) {
		Session session = Sessions.getSession(ID);
		try {
			payload = URLDecoder.decode(payload, "UTF-8");
			System.err.println(payload);
			if (session == null)
				throw new SessionNotFoundException();
				
			Mission mission = JsonBridge.json2mission(payload);
			if (mission == null) 
				throw new Exception("Impossible to create the Mission model!");
			
			System.err.println("Mission: " + mission.getName());
			session.setMission(mission);
			session.setJsonMission(payload);
			
			httpServletResponse.setStatus(HttpServletResponse.SC_OK);
		}
		catch (Exception e) {
			try {
				e.printStackTrace();
				String message = "";
				if (e instanceof JsonParseException) message = "Json sintax error!";
				else message = e.getMessage();
				httpServletResponse.sendError(HttpServletResponse.SC_NOT_FOUND, 
												"FlyaqError: " + message);
			} catch (Exception e1) { e1.printStackTrace(); }
		}
	}
}
