import React from 'react'
import { Routes, Route } from 'react-router-dom'
import Main from '~@/Layout/jsx/Main'
import Footer from '~@/Layout/jsx/Footer'
import NotFoundPage from '~@/Layout/jsx/NotFoundPage'
import VerifyEmail from '~@/Authorization/jsx/VerifyEmail'
import ChangePassword from '~@/Authorization/jsx/ChangePassword'
import ContinueRegistration from '~@/Authorization/jsx/ContinueRegistration'
import ConfirmEmail from '~@/Authorization/jsx/ConfirmEmail'
import UserBasicInfo from '~@/UserArea/jsx/UserBasicInfo'
import ChooseRole from '~@/ChooseRoleSteps/jsx/ChooseRole'
import FullCalendar from '~@/WorkRooms/FullCalendar'
import CreateEvent from '~@/CreateEvent/CreateEvent'

function App() {
  //   const isAuthentikated = !!token;

  return (
    <>
      <main>
        <Routes>
          <Route path='/' element={<Main />} />
          <Route path='/verify_email' element={<VerifyEmail />} />
          <Route path='/confirm_email' element={<ConfirmEmail />} />
          <Route
            path='/continue_registration'
            element={<ContinueRegistration />}
          />
          <Route path='/user_basic-info' element={<UserBasicInfo />} />
          <Route path='/user_choose-role' element={<ChooseRole />} />
          <Route path='/user_profile' element={<FullCalendar />} />
          <Route path='/create_event' element={<CreateEvent />} />
          <Route path='/change_password' element={<ChangePassword />} />
          <Route path='*' element={<NotFoundPage />} />
        </Routes>
      </main>
      <Footer />
    </>
  )
}

export default App
